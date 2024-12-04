# PLC Data Integration to MySQL Database

Este proyecto está diseñado para leer datos de un PLC utilizando `snap7` y almacenarlos en una base de datos MySQL. Los datos leídos incluyen información de tiempo, caudal, presión y otros parámetros que se almacenan en una tabla de MySQL para su posterior análisis.

## Requisitos

Antes de ejecutar el proyecto, asegúrate de tener los siguientes paquetes instalados:

- `snap7` - Para la comunicación con el PLC.
- `mysql-connector-python` - Para la interacción con la base de datos MySQL.
- `pandas`, `numpy` - Para el manejo de datos.
  
Puedes instalar estos paquetes utilizando el archivo `requirements.txt` o `environment.yml` que se incluye en el repositorio.

## Instalación

### Usando `requirements.txt`:

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio

2. Clona el repositorio:
   ```bash
   pip install -r requirements.txt

### Usando environment.yml (Conda):

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio

2. Crea un entorno Conda desde el archivo `environment.yml`
   ```bash
   conda env create -f environment.yml

3. Activa el entorno:
   ```bash
   conda activate tu_entorno

### Uso

1. Conecta el PLC a tu red local.
2. Asegúrate de que el servidor MySQL esté en funcionamiento y que la base de datos `tu_database` esté configurada correctamente.
3. Ejecuta el script plc_reader.py para empezar a leer los datos del PLC y almacenarlos en la base de datos:
    ```bash
    python plc_reader.py

### Contribuciones

Las contribuciones son bienvenidas. Si encuentras algún problema o tienes una idea para mejorar este proyecto, por favor abre un `issue` o crea un `pull request`.
