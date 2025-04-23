import threading
import random
from datetime import datetime
from ..classes.estacion import Estacion
from ..classes.registro_climatico import RegistroClimatico
from ..classes.lista import Lista
from ..classes.tabla_hash import TablaHash
from ..classes.encryption import Encryption
from ..functions.lista_insertar import insertar
from ..functions.lista_buscar import buscar as lista_buscar
from ..functions.lista_barrido import barrido
from ..functions.hash_agregar import agregar
from ..functions.hash_buscar import buscar as hash_buscar
from ..functions.encrypt_encrypt import encrypt
from ..functions.encrypt_decrypt import decrypt
from ..database import Database

class Controller:
    """Clase que gestiona la lógica del sistema MVC."""
    def __init__(self):
        print("Inicializando Controller...")
        self.db = Database()
        self.estaciones_lista = Lista()
        self.estaciones_tabla = TablaHash(9)
        self.encryption = Encryption()
        self.timer = None
        self.is_running = False
        self.id_estacion_periodica = None
        self.db.cargar_datos(self.estaciones_lista, self.estaciones_tabla)

    def agregar_estacion(self, id_estacion, nombre, ubicacion):
        """Agrega una estación a la lista, la tabla hash y la base de datos."""
        try:
            print(f"Valores recibidos - id_estacion: {id_estacion}, nombre: {nombre}, ubicacion: {ubicacion}")
            if not id_estacion or not nombre or not ubicacion:
                return "Error: Todos los campos (ID, Nombre, Ubicación) son requeridos"
            
            print("Creando objeto Estacion...")
            estacion = Estacion(id_estacion, nombre, ubicacion)
            print(f"Estacion creada: id={estacion.id_estacion}, nombre={estacion.nombre}, ubicacion={estacion.ubicacion}")
            
            print("Insertando en la lista de listas...")
            insertar(self.estaciones_lista, estacion, campo='id_estacion')
            print("Estación insertada en la lista de listas")
            
            print("Insertando en la tabla hash...")
            agregar(self.estaciones_tabla, estacion)
            print("Estación insertada en la tabla hash")
            
            print("Guardando en la base de datos...")
            self.db.guardar_estacion(estacion)
            print("Estación guardada en la base de datos")
            
            return f"Estación {nombre} añadida con éxito"
        except Exception as e:
            print(f"Error capturado en agregar_estacion: {str(e)}")
            return f"Error al agregar estación: {str(e)}"

    def agregar_registro(self, id_estacion, fecha, temperatura, humedad):
        """Agrega un registro climático cifrado a la sublista y la base de datos."""
        try:
            print(f"Valores recibidos - id_estacion: {id_estacion}, fecha: {fecha}, temperatura: {temperatura}, humedad: {humedad}")
            if not id_estacion or not fecha or temperatura is None or humedad is None:
                return "Error: Todos los campos (ID, Fecha, Temperatura, Humedad) son requeridos"
            
            print("Buscando estación en la lista...")
            nodo = lista_buscar(self.estaciones_lista, id_estacion, campo='id_estacion')
            if nodo:
                print("Creando registro...")
                registro = RegistroClimatico(fecha, temperatura, humedad)
                print("Cifrando registro...")
                encrypted_registro = encrypt(self.encryption, registro)
                print("Insertando registro en la sublista...")
                insertar(nodo.sublista, encrypted_registro, campo=None)
                print("Guardando registro en la base de datos...")
                self.db.guardar_registro(id_estacion, encrypted_registro)
                print("Registro guardado en la base de datos")
                return f"Registro añadido a estación {id_estacion}"
            return f"Estación {id_estacion} no encontrada"
        except Exception as e:
            print(f"Error capturado en agregar_registro: {str(e)}")
            return f"Error al agregar registro: {str(e)}"

    def buscar_estacion(self, id_estacion):
        """Busca una estación en la tabla hash."""
        estacion = hash_buscar(self.estaciones_tabla, id_estacion)
        if estacion:
            return str(estacion)
        return "Estación no encontrada"

    def mostrar_datos(self):
        """Muestra todas las estaciones y sus registros descifrados."""
        output = []
        aux = self.estaciones_lista.inicio
        while aux:
            output.append(str(aux.info))
            if aux.sublista:
                output.append("  Registros:")
                nodo = aux.sublista.inicio
                while nodo:
                    if isinstance(nodo.info, str):
                        try:
                            decrypted_data = decrypt(self.encryption, nodo.info)
                            registro = RegistroClimatico(
                                decrypted_data['fecha'],
                                decrypted_data['temperatura'],
                                decrypted_data['humedad']
                            )
                            output.append(f"    {registro}")
                        except Exception as e:
                            output.append(f"    Error al descifrar: {e}")
                    else:
                        output.append(f"    {nodo.info}")
                    nodo = nodo.sig
            aux = aux.sig
        return "\n".join(output) if output else "No hay estaciones"

    def generar_registro_simulado(self):
        """Genera un registro climático simulado."""
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        temperatura = round(random.uniform(15, 35), 1)
        humedad = random.randint(40, 90)
        return fecha, temperatura, humedad

    def agregar_registro_periodico(self):
        """Añade un registro simulado cada N segundos a la estación seleccionada."""
        if not self.is_running or not self.id_estacion_periodica:
            return
        
        fecha, temperatura, humedad = self.generar_registro_simulado()
        result = self.agregar_registro(self.id_estacion_periodica, fecha, temperatura, humedad)
        print(f"Registro periódico añadido: {result}")
        
        if self.is_running:
            self.timer = threading.Timer(10, self.agregar_registro_periodico)
            self.timer.start()

    def iniciar_guardado_periodico(self, id_estacion):
        """Inicia el guardado periódico para una estación."""
        if self.is_running:
            return "Guardado periódico ya está en ejecución"
        
        if not hash_buscar(self.estaciones_tabla, id_estacion):
            return f"Estación {id_estacion} no encontrada"
        
        self.id_estacion_periodica = id_estacion
        self.is_running = True
        self.timer = threading.Timer(10, self.agregar_registro_periodico)
        self.timer.start()
        return f"Guardado periódico iniciado para estación {id_estacion}"

    def detener_guardado_periodico(self):
        """Detiene el guardado periódico."""
        if not self.is_running:
            return "Guardado periódico no está en ejecución"
        
        self.is_running = False
        if self.timer:
            self.timer.cancel()
            self.timer = None
        self.id_estacion_periodica = None
        return "Guardado periódico detenido"

    def close(self):
        """Cierra los recursos al finalizar."""
        self.detener_guardado_periodico()
        self.db.close()
        


# Propósito: La clase Controller centraliza la lógica del sistema, interactuando con el modelo (lista de listas, tabla hash, cifrado) y preparando datos para la vista (Gradio).

# Atributos:
# estaciones_lista: Lista de listas para almacenar estaciones y sus registros cifrados.

# estaciones_tabla: Tabla hash para búsquedas rápidas por id_estacion.

# encryption: Instancia de Encryption para cifrar/descrifrar registros.

# Métodos:
# agregar_estacion: Crea una Estacion y la inserta en la lista y la tabla hash.

# agregar_registro: Busca una estación, cifra un RegistroClimatico, y lo inserta en su sublista.

# buscar_estacion: Busca una estación en la tabla hash y retorna su representación como string.

# mostrar_datos: Recorre la lista de listas, descifra los registros, y retorna una string con todos los datos.

# Sin diccionarios: Usa listas enlazadas, arreglos, y strings, con un diccionario temporal solo para JSON en cifrado.

# Granularidad: La clase está en un archivo separado, y usa funciones externas en functions/.

# Uso: Estos métodos serán llamados por la interfaz Gradio para gestionar el sistema.

# Tras implementar el guardado periódico:

# Nuevos Atributos:
# timer: Almacena el objeto threading.Timer para el guardado periódico.

# is_running: Indica si el temporizador está activo.

# id_estacion_periodica: Almacena el ID de la estación para la que se generan registros.

# Nuevos Métodos:
# generar_registro_simulado: Crea un registro simulado con fecha actual, temperatura aleatoria (15-35°C), y humedad aleatoria (40-90%).

# agregar_registro_periodico: Genera un registro simulado, lo cifra, y lo inserta en la sublista de la estación seleccionada. Reprograma el temporizador si sigue activo.

# iniciar_guardado_periodico: Inicia el temporizador para la estación especificada, ejecutando agregar_registro_periodico cada 10 segundos.

# detener_guardado_periodico: Detiene el temporizador y limpia el estado.

# Temporizador:
# Usa threading.Timer para ejecutar agregar_registro_periodico cada 10 segundos (intervalo arbitrario, ya que no se especificó uno).

# El temporizador se reprograma automáticamente mientras is_running sea True.

# Sin diccionarios: Usa las estructuras existentes (listas, arreglos) y solo genera datos primitivos.

# Granularidad: Los nuevos métodos están dentro de controller.py, pero podríamos separarlos en archivos individuales si el profesor lo exige más adelante.

# Uso: Permite generar registros automáticamente, cumpliendo el requisito de "cada N tiempo se guarde algo".

# Tras añadir la BD:

# Nuevos Atributos:
# db: Instancia de Database para manejar la base de datos.

# Cambios:
# En __init__, creamos la base de datos y cargamos los datos existentes con self.db.cargar_datos.

# En agregar_estacion y agregar_registro, guardamos los datos en la base de datos con self.db.guardar_estacion y self.db.guardar_registro.

# Añadimos un método close para cerrar la conexión a la base de datos al finalizar.

# Sin diccionarios: Usa las estructuras existentes y consultas SQL.

# Uso: Persiste los datos entre ejecuciones, cargándolos al iniciar y guardándolos al añadir.

