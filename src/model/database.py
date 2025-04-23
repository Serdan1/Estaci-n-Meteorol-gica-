import sqlite3
from .classes.estacion import Estacion
from .classes.lista import Lista
from .functions.lista_insertar import insertar
from .functions.hash_agregar import agregar

class Database:
    """Clase para manejar la base de datos SQLite."""
    def __init__(self, db_name="weather_station.db"):
        print(f"Inicializando base de datos: {db_name}")
        try:
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
            self.create_tables()
        except sqlite3.Error as e:
            print(f"Error al conectar a la base de datos: {str(e)}")
            raise

    def create_tables(self):
        """Crea las tablas si no existen."""
        print("Creando tablas en la base de datos...")
        try:
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
            print("Tablas creadas con éxito")
        except sqlite3.Error as e:
            print(f"Error al crear tablas: {str(e)}")
            raise

    def guardar_estacion(self, estacion):
        """Guarda una estación en la base de datos."""
        try:
            print(f"Guardando estación: id={estacion.id_estacion}, nombre={estacion.nombre}, ubicacion={estacion.ubicacion}")
            # Validar datos antes de guardar
            if not estacion.id_estacion or not estacion.nombre or not estacion.ubicacion:
                raise ValueError("Todos los campos (id_estacion, nombre, ubicacion) deben tener valores no vacíos")
            
            self.cursor.execute('''
                INSERT OR REPLACE INTO estaciones (id_estacion, nombre, ubicacion)
                VALUES (?, ?, ?)
            ''', (estacion.id_estacion, estacion.nombre, estacion.ubicacion))
            self.conn.commit()
            print("Estación guardada con éxito en la base de datos")
            # Verificar que se guardó correctamente
            self.cursor.execute('SELECT * FROM estaciones WHERE id_estacion = ?', (estacion.id_estacion,))
            result = self.cursor.fetchone()
            print(f"Verificación - Datos guardados: {result}")
        except sqlite3.Error as e:
            print(f"Error de SQLite al guardar estación: {str(e)}")
            raise Exception(f"Error al guardar estación en la base de datos: {str(e)}")
        except AttributeError as e:
            print(f"Error de atributo al guardar estación: {str(e)}")
            raise Exception(f"Error de atributo al guardar estación: {str(e)}")
        except ValueError as e:
            print(f"Error de validación al guardar estación: {str(e)}")
            raise

    def guardar_registro(self, id_estacion, encrypted_data):
        """Guarda un registro cifrado en la base de datos."""
        try:
            print(f"Guardando registro: id_estacion={id_estacion}, data={encrypted_data}")
            self.cursor.execute('''
                INSERT INTO registros (id_estacion, data)
                VALUES (?, ?)
            ''', (id_estacion, encrypted_data))
            self.conn.commit()
            print("Registro guardado con éxito")
        except sqlite3.Error as e:
            print(f"Error de SQLite al guardar registro: {str(e)}")
            raise Exception(f"Error al guardar registro: {str(e)}")

    def cargar_datos(self, lista, tabla):
        """Carga estaciones y registros desde la base de datos al iniciar."""
        print("Cargando datos desde la base de datos...")
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
        print("Datos cargados con éxito")

    def close(self):
        """Cierra la conexión a la base de datos."""
        print("Cerrando la conexión a la base de datos...")
        self.conn.close()
        