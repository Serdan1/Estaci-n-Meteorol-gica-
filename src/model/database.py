import sqlite3
from .classes.estacion import Estacion
from .classes.lista import Lista
from .functions.lista_insertar import insertar
from .functions.hash_agregar import agregar

class Database:
    """Clase para manejar la base de datos SQLite."""
    def __init__(self, db_name="weather_station.db"):
        self.db_name = db_name
        self.create_tables()

    def _get_connection(self):
        """Crea una nueva conexión a la base de datos en el hilo actual."""
        print(f"Creando nueva conexión a la base de datos: {self.db_name}")
        return sqlite3.connect(self.db_name)

    def create_tables(self):
        """Crea las tablas si no existen."""
        print("Creando tablas en la base de datos...")
        conn = self._get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS estaciones (
                    id_estacion TEXT PRIMARY KEY,
                    nombre TEXT NOT NULL,
                    ubicacion TEXT NOT NULL
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS registros (
                    id_registro INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_estacion TEXT NOT NULL,
                    data TEXT NOT NULL,
                    FOREIGN KEY (id_estacion) REFERENCES estaciones(id_estacion)
                )
            ''')
            conn.commit()
            print("Tablas creadas con éxito")
        except sqlite3.Error as e:
            print(f"Error al crear tablas: {str(e)}")
            raise
        finally:
            conn.close()

    def guardar_estacion(self, estacion):
        """Guarda una estación en la base de datos."""
        conn = self._get_connection()
        cursor = conn.cursor()
        try:
            print(f"Guardando estación: id={estacion.id_estacion}, nombre={estacion.nombre}, ubicacion={estacion.ubicacion}")
            if not estacion.id_estacion or not estacion.nombre or not estacion.ubicacion:
                raise ValueError("Todos los campos (id_estacion, nombre, ubicacion) deben tener valores no vacíos")
            
            cursor.execute('''
                INSERT OR REPLACE INTO estaciones (id_estacion, nombre, ubicacion)
                VALUES (?, ?, ?)
            ''', (estacion.id_estacion, estacion.nombre, estacion.ubicacion))
            conn.commit()
            print("Estación guardada con éxito en la base de datos")
            cursor.execute('SELECT * FROM estaciones WHERE id_estacion = ?', (estacion.id_estacion,))
            result = cursor.fetchone()
            print(f"Verificación - Datos guardados: {result}")
        except sqlite3.Error as e:
            print(f"Error de SQLite al guardar estación: {str(e)}")
            raise Exception(f"Error al guardar estación: {str(e)}")
        except AttributeError as e:
            print(f"Error de atributo al guardar estación: {str(e)}")
            raise Exception(f"Error de atributo al guardar estación: {str(e)}")
        except ValueError as e:
            print(f"Error de validación al guardar estación: {str(e)}")
            raise
        finally:
            conn.close()

    def guardar_registro(self, id_estacion, encrypted_data):
        """Guarda un registro cifrado en la base de datos."""
        conn = self._get_connection()
        cursor = conn.cursor()
        try:
            print(f"Guardando registro: id_estacion={id_estacion}, data={encrypted_data}")
            cursor.execute('''
                INSERT INTO registros (id_estacion, data)
                VALUES (?, ?)
            ''', (id_estacion, encrypted_data))
            conn.commit()
            print("Registro guardado con éxito")
        except sqlite3.Error as e:
            print(f"Error de SQLite al guardar registro: {str(e)}")
            raise Exception(f"Error al guardar registro: {str(e)}")
        finally:
            conn.close()

    def cargar_datos(self, lista, tabla):
        """Carga estaciones y registros desde la base de datos al iniciar."""
        conn = self._get_connection()
        cursor = conn.cursor()
        try:
            print("Cargando datos desde la base de datos...")
            cursor.execute('SELECT id_estacion, nombre, ubicacion FROM estaciones')
            for row in cursor.fetchall():
                estacion = Estacion(row[0], row[1], row[2])
                insertar(lista, estacion, campo='id_estacion')
                agregar(tabla, estacion)

            cursor.execute('SELECT id_estacion, data FROM registros')
            for row in cursor.fetchall():
                id_estacion, encrypted_data = row
                from .functions.lista_buscar import buscar as lista_buscar
                nodo = lista_buscar(lista, id_estacion, campo='id_estacion')
                if nodo:
                    insertar(nodo.sublista, encrypted_data, campo=None)
            print("Datos cargados con éxito")
        finally:
            conn.close()

    def close(self):
        """No se necesita cerrar ninguna conexión persistente."""
        print("Cerrando Database (no hay conexiones persistentes para cerrar)")

