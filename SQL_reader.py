# SQL_reader.py
import time
import mysql.connector
from plc_reader import connect_to_plc, read_process_data

def connect_to_db():
    """Conecta a la base de datos MySQL."""
    try:
        db_connection = mysql.connector.connect(
            host="localhost",  # Cambia por la IP de tu servidor de base de datos
            user="root",       # Cambia por tu usuario de MySQL
            password="root",   # Cambia por tu contraseña de MySQL
            database="armada_database"  # Cambia por el nombre de tu base de datos
        )
        
        if db_connection.is_connected():
            print("Conexión exitosa a la base de datos")
            return db_connection
    except mysql.connector.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def insert_data(cursor, tiempo, tiemposuministro, caudal, presion, muellenum):
    """Inserta los datos en la base de datos."""
    insert_query = """
    INSERT INTO armada (tiempo, tiemposuministro, caudal, presion, muellenum)
    VALUES (%s, %s, %s, %s, %s)
    """
    values = (tiempo, tiemposuministro, caudal, presion, muellenum)
    cursor.execute(insert_query, values)

def main():
    # Conectar al PLC
    ip_plc = '127.0.0.1'  # Dirección IP del PLC
    rack = 0
    slot = 1
    db_number = 54  # Cambia por el número de tu DB
    start_address = 0  # Cambia por la dirección de inicio de tu DB
    plc = connect_to_plc(ip_plc, rack, slot)

    if plc is None:
        return

    # Conectar a la base de datos
    db_connection = connect_to_db()
    if db_connection is None:
        return

    cursor = db_connection.cursor()

    try:
        while True:
            # Leer datos del PLC
            datos = read_process_data(plc, db_number, start_address)

            # Verificar si los datos son válidos
            if datos['tiempo'] and datos['tiemposuministro'] is not None:
                # Insertar datos en la base de datos
                insert_data(cursor, datos['tiempo'], datos['tiemposuministro'], datos['caudal'], datos['presion'], datos['muellenum'])

                # Confirmar la transacción
                db_connection.commit()
                print(f"Datos insertados: {datos}")

            # Esperar un intervalo antes de la siguiente lectura
            time.sleep(5)  # Espera 5 segundos

    except Exception as e:
        print(f"Error durante la inserción de datos: {e}")
    finally:
        # Cerrar cursor y conexión
        if db_connection.is_connected():
            cursor.close()
            db_connection.close()
            print("Conexión cerrada")

if __name__ == "__main__":
    main()