# Estación-Meteorológica-

https://github.com/Serdan1/Estaci-n-Meteorol-gica-.git


# Estación Meteorológica

Sistema para gestionar estaciones meteorológicas con datos climáticos almacenados en una lista de listas dinámica, una tabla hash, y una base de datos SQLite, con cifrado AES. Implementado en Python con una interfaz MVC usando Gradio.

## Características
- **Lista de listas dinámica**: Almacena estaciones y sus registros climáticos (Figura 13).
- **Tabla hash**: Permite búsquedas rápidas de estaciones por ID (Figura 1).
- **Cifrado**: Los registros climáticos se almacenan cifrados con AES.
- **Persistencia**: Datos guardados en una base de datos SQLite (`weather_station.db`).
- **Interfaz Gradio**: Interfaz gráfica para agregar estaciones, registros, buscar, y mostrar datos.
- **Guardado Periódico**: Añade registros simulados cada 10 segundos a una estación seleccionada.

## Estructura del Proyecto
- `src/model/classes/`: Clases como `Estacion`, `Lista`, `TablaHash`, `Encryption`.
- `src/model/functions/`: Funciones como `insertar`, `buscar`, `encrypt`, `decrypt`.
- `src/model/database.py`: Manejo de la base de datos SQLite.
- `src/model/controller/`: Controlador MVC (`controller.py`).
- `src/view/`: Interfaz Gradio (`interface.py`).
- `tests/`: Pruebas unitarias.
- `main.py`: Punto de entrada que lanza la interfaz.

## Instalación
1. Clona el repositorio:
   ```bash
   git clone <URL>
   cd weather-station

Instala las dependencias:
bash

pip install -r docs/requirements.txt

Ejecuta el sistema:
bash

python main.py

Abre la URL generada por Gradio (ej. http://127.0.0.1:7860) en un navegador.



## USO
Agregar Estación: Ingresa ID, nombre y ubicación.

Agregar Registro: Ingresa ID de estación, fecha, temperatura y humedad.

Buscar Estación: Busca por ID.

Mostrar Datos: Muestra todas las estaciones y registros descifrados.

Guardado Periódico: Inicia/detiene la generación automática de registros cada 10 segundos.



Persistencia
Los datos se guardan en una base de datos SQLite (weather_station.db):
Tabla estaciones: Almacena ID, nombre y ubicación de las estaciones.

Tabla registros: Almacena registros climáticos cifrados con referencia a la estación.



## Pruebas
Ejecuta las pruebas unitarias para verificar la funcionalidad:

python -m unittest discover tests



## Requisitos cumplidos
Estructura de lista de listas dinámica

Tabla hash para acceso rápido 

Cifrado de registros con AES.

Persistencia con SQLite.

Interfaz MVC con Gradio.

Guardado periódico de registros simulados.


# Estación Meteorológica

Sistema para gestionar estaciones meteorológicas con datos climáticos almacenados en una lista de listas dinámica, una tabla hash, y una base de datos SQLite, con cifrado AES. Implementado en Python con una interfaz MVC usando Gradio.

## Arquitectura

El sistema sigue el patrón **Modelo-Vista-Controlador (MVC)**. A continuación, se muestra un diagrama que representa la interacción entre los componentes principales:

```mermaid
flowchart TD
    A[Usuario] -->|Interacciona| B[Vista: Gradio]
    B -->|Llama métodos| C[Controlador: Controller]
    C -->|Gestiona datos| D[Modelo: Lista de Listas y Tabla Hash]
    C -->|Guarda y carga datos| E[Base de Datos: SQLite]
    D -->|Almacena datos en memoria| C
    E -->|Persiste datos| C