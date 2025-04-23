from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import json

class Encryption:
    """Clase para cifrar y descifrar datos usando AES."""
    def __init__(self, key=None):
        # Si no se proporciona una clave, generar una de 16 bytes
        self.key = key if key else get_random_bytes(16)
        self.cipher = None

    def pad(self, data):
        """Rellena los datos para que sean múltiplos de 16 bytes."""
        padding_length = 16 - (len(data) % 16)
        return data + (chr(padding_length) * padding_length).encode()

    def unpad(self, data):
        """Elimina el relleno de los datos descifrados."""
        padding_length = data[-1]
        return data[:-padding_length]

    def encrypt(self, data):
        """Cifra un diccionario de datos y devuelve el texto cifrado en base64."""
        # Convertir datos a JSON
        data_json = json.dumps(data).encode()
        # Rellenar datos
        data_padded = self.pad(data_json)
        # Generar IV (vector de inicialización)
        iv = get_random_bytes(16)
        # Crear cifrador
        self.cipher = AES.new(self.key, AES.MODE_CBC, iv)
        # Cifrar
        encrypted_data = self.cipher.encrypt(data_padded)
        # Combinar IV y datos cifrados, codificar en base64
        return base64.b64encode(iv + encrypted_data).decode('utf-8')

    def decrypt(self, encrypted_data):
        """Descifra un texto cifrado en base64 y devuelve el diccionario original."""
        # Decodificar de base64
        raw = base64.b64decode(encrypted_data)
        # Extraer IV (primeros 16 bytes) y datos cifrados
        iv, encrypted_data = raw[: рыб

System: You are Grok 3 built by xAI.

I'm here to help you create the code for your weather station project step by step, ensuring it meets all the requirements: a dynamic list of lists structure (Figura 13), a hash table (Figura 1), encrypted data using AES (not hash-based encryption), and an MVC interface with Gradio. We'll avoid using dictionaries as requested and proceed gradually. You've confirmed using Gradio for the interface, and we've outlined a project structure. Let's continue with the next steps after implementing `station.py` and `encryption.py`.

---

### **Paso 3: Implementar `tda_lista_lista.py`**
This file will implement the **TDA lista de listas dinámica** based on Figura 13 (page 65 of the document). It will define a dynamic list where each node in the main list (representing weather stations) contains a sublist (representing climatic records). We'll adapt the code from the document, ensuring no dictionaries are used and supporting the station and record classes.

**Archivo**: `src/model/tda_lista_lista.py`

```python
from .station import Estacion, RegistroClimatico

class NodoLista:
    """Clase para nodos de la lista."""
    def __init__(self):
        self.info = None  # Almacena Estacion o RegistroClimatico
        self.sig = None   # Siguiente nodo
        self.sublista = None  # Sublista para registros climáticos

class Lista:
    """Clase para lista simplemente enlazada dinámica."""
    def __init__(self):
        self.inicio = None
        self.tamanio = 0

    def insertar(self, dato, campo=None):
        """Inserta un dato en la lista de forma ordenada."""
        nodo = NodoLista()
        nodo.info = dato
        # Si es un nodo de la lista principal (Estacion), inicializar sublista
        if isinstance(dato, Estacion):
            nodo.sublista = Lista()

        if self.inicio is None or self.comparar(self.inicio.info, dato, campo) > 0:
            nodo.sig = self.inicio
            self.inicio = nodo
        else:
            ant, act = self.inicio, self.inicio.sig
            while act and self.comparar(act.info, dato, campo) < 0:
                ant, act = act, act.sig
            nodo.sig = act
            ant.sig = nodo
        self.tamanio += 1

    def buscar(self, buscado, campo=None):
        """Busca un elemento en la lista."""
        aux = self.inicio
        while aux and self.comparar(aux.info, buscado, campo) != 0:
            aux = aux.sig
        return aux

    def eliminar(self, clave, campo=None):
        """Elimina un elemento de la lista y lo devuelve."""
        dato = None
        if self.inicio and self.comparar(self.inicio.info, clave, campo) == 0:
            dato = self.inicio.info
            self.inicio = self.inicio.sig
            self.tamanio -= 1
        else:
            ant, act = self.inicio, self.inicio.sig
            while act and self.comparar(act.info, clave, campo) != 0:
                ant, act = act, act.sig
            if act:
                dato = act.info
                ant.sig = act.sig
                self.tamanio -= 1
        return dato

    def barrido(self):
        """Recorre la lista mostrando sus valores."""
        aux = self.inicio
        while aux:
            print(str(aux.info))
            if aux.sublista:
                print("  Registros:")
                aux.sublista.barrido()
            aux = aux.sig

    def comparar(self, info1, info2, campo=None):
        """Compara dos elementos según el campo especificado."""
        val1 = self.obtener_valor(info1, campo)
        val2 = self.obtener_valor(info2, campo)
        if val1 < val2:
            return -1
        elif val1 > val2:
            return 1
        return 0

    def obtener_valor(self, info, campo):
        """Obtiene el valor de un campo sin usar diccionarios."""
        if campo is None:
            return info
        if isinstance(info, Estacion):
            if campo == 'id_estacion':
                return info.id_estacion
            elif campo == 'nombre':
                return info.nombre
            elif campo == 'ubicacion':
                return info.ubicacion
        elif isinstance(info, RegistroClimatico):
            if campo == 'fecha':
                return info.fecha
            elif campo == 'temperatura':
                return info.temperatura
            elif campo == 'humedad':
                return info.humedad
        return info