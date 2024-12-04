# plc_reader.py
import snap7
from snap7.util import get_int, get_byte, get_real
from datetime import datetime, timedelta

def connect_to_plc(ip, rack, slot):
    """Conecta al PLC."""
    plc = snap7.client.Client()
    plc.connect(ip, rack, slot)
    if not plc.get_connected():
        raise Exception("No se pudo conectar al PLC")
    print("Conectado al PLC")
    return plc

def read_dtl(plc, db_number, start_address):
    """Lee el DTL desde el PLC."""
    dtl_size = 12  # Tamaño total del DTL
    data = plc.db_read(db_number, start_address, dtl_size)
    print(f"Raw DTL data: {data.hex()}")

    year = get_int(data, 0)  # Offset 0
    month = get_byte(data, 2)  # Offset 2
    day = get_byte(data, 3)  # Offset 3
    weekday = get_byte(data, 4)  # Offset 4 - Día de la semana
    hour = get_byte(data, 5)  # Offset 5
    minute = get_byte(data, 6)  # Offset 6
    second = get_byte(data, 7)  # Offset 7
    nanosecond = get_int(data, 8)  # Offset 8 - Nanosegundos (si es necesario)

    # Crear objeto datetime
    return datetime(year, month, day, hour, minute, second)

def read_process_data(plc, db_number, start_address):
    """Lee los datos del proceso desde el PLC."""
    # Leer tiemposuministro (TIME) desde el offset 0
    tiemposuministro_data = plc.db_read(db_number, start_address, 4)  # 4 bytes para TIME
    tiemposuministro_milisegundos = snap7.util.get_dword(tiemposuministro_data, 0)  # Obtener el valor en milisegundos
    
    # Convertir el valor de TIME (milisegundos) a un objeto timedelta
    tiemposuministro_timedelta = timedelta(milliseconds=tiemposuministro_milisegundos)

    # Leer caudal y presión (REAL)
    caudal = get_real(plc.db_read(db_number, 4, 4), 0)  # Offset 4.0
    presion = get_real(plc.db_read(db_number, 8, 4), 0)  # Offset 8.0

    # Leer DTL
    tiempo = read_dtl(plc, db_number, 12)  # Offset 12.0

    # Leer número de muelle (INT)
    muellenum = get_int(plc.db_read(db_number, 24, 2), 0)  # Offset 24.0

    return {
        "tiempo": tiempo,
        "tiemposuministro": tiemposuministro_timedelta,
        "caudal": caudal,
        "presion": presion,
        "muellenum": muellenum,
    }
