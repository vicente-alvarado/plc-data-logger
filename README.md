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
