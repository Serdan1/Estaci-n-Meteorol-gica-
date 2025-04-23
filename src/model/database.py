import sqlite3
from .classes.estacion import Estacion
from .classes.lista import Lista
from .functions.lista_insertar import insertar
from .functions.hash_agregar import agregar

class Database:
    """Clase para manejar la base de datos SQLite."""
    def __init__(self, db_name="weather_station.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """Crea las tablas si no existen."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS estaciones (
                id_estacion TEXT PRIMARY KEY,
                nombre TEXT NOT NULL,
                ubicacion TEXT NOT NULL
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS registros (
                id_registro INTEGER PRIMARY KEY AUTOINCREMENT,
                id_estacion TEXT NOT NULL,
                data TEXT NOT NULL,
                FOREIGN KEY (id_estacion) REFERENCES estaciones(id_estacion)
            )
        ''')
        self.conn.commit()

    def guardar_estacion(self, estacion):
        """Guarda una estación en la base de datos."""
        self.cursor.execute('''
            INSERT OR REPLACE INTO estaciones (id_estacion, nombre, ubicacion)
            VALUES (?, ?, ?)
        ''', (estacion.id_estacion, estacion.nombre, estacion.ubicacion))
        self.conn.commit()

    def guardar_registro(self, id_estacion, encrypted_data):
        """Guarda un registro cifrado en la base de datos."""
        self.cursor.execute('''
            INSERT INTO registros (id_estacion, data)
            VALUES (?, ?)
        ''', (id_estacion, encrypted_data))
        self.conn.commit()

    def cargar_datos(self, lista, tabla):
        """Carga estaciones y registros desde la base de datos al iniciar."""
        self.cursor.execute('SELECT id_estacion, nombre, ubicacion FROM estaciones')
        for row in self.cursor.fetchall():
            estacion = Estacion(row[0], row[1], row[2])
            insertar(lista, estacion, campo='id_estacion')
            agregar(tabla, estacion)

        self.cursor.execute('SELECT id_estacion, data FROM registros')
        for row in self.cursor.fetchall():
            id_estacion, encrypted_data = row
            from .functions.lista_buscar import buscar as lista_buscar
            nodo = lista_buscar(lista, id_estacion, campo='id_estacion')
            if nodo:
                insertar(nodo.sublista, encrypted_data, campo=None)

    def close(self):
        """Cierra la conexión a la base de datos."""
        self.conn.close()

# Propósito: Maneja la base de datos SQLite para almacenar estaciones y registros.

# Métodos:
# create_tables: Crea las tablas estaciones y registros.

# guardar_estacion: Inserta o actualiza una estación en la tabla estaciones.

# guardar_registro: Inserta un registro cifrado en la tabla registros.

# cargar_datos: Carga los datos al iniciar el sistema, reconstruyendo la lista de listas y la tabla hash.

# close: Cierra la conexión a la base de datos.

# Sin diccionarios: Usa consultas SQL y las estructuras existentes (listas, arreglos).

# Granularidad: La clase está en un archivo separado, siguiendo las preferencias del profesor.

