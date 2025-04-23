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

class Controller:
    """Clase que gestiona la lógica del sistema MVC."""
    def __init__(self):
        self.estaciones_lista = Lista()  # Lista de listas para estaciones
        self.estaciones_tabla = TablaHash(9)  # Tabla hash con tamaño 9
        self.encryption = Encryption()  # Instancia para cifrado

    def agregar_estacion(self, id_estacion, nombre, ubicacion):
        """Agrega una estación a la lista y la tabla hash."""
        estacion = Estacion(id_estacion, nombre, ubicacion)
        insertar(self.estaciones_lista, estacion, campo='id_estacion')
        agregar(self.estaciones_tabla, estacion)
        return f"Estación {nombre} añadida con éxito"

    def agregar_registro(self, id_estacion, fecha, temperatura, humedad):
        """Agrega un registro climático cifrado a la sublista de una estación."""
        nodo = lista_buscar(self.estaciones_lista, id_estacion, campo='id_estacion')
        if nodo:
            registro = RegistroClimatico(fecha, temperatura, humedad)
            encrypted_registro = encrypt(self.encryption, registro)
            insertar(nodo.sublista, encrypted_registro, campo=None)
            return f"Registro añadido a estación {id_estacion}"
        return f"Estación {id_estacion} no encontrada"

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
                            decrypted_data = self.encryption.decrypt(nodo.info)
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

