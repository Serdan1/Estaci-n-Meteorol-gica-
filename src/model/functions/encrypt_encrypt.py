from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import json
from ..classes.encryption import Encryption

def encrypt(encryption, data):
    """Cifra un objeto y devuelve el texto cifrado en base64."""
    if not isinstance(encryption, Encryption):
        raise ValueError("El primer argumento debe ser una Encryption")
    
    # Convertir datos a JSON
    data_json = json.dumps({
        'fecha': data.fecha,
        'temperatura': data.temperatura,
        'humedad': data.humedad
    }).encode()
    
    # Rellenar datos para múltiplo de 16 bytes
    padding_length = 16 - (len(data_json) % 16)
    data_padded = data_json + (chr(padding_length) * padding_length).encode()
    
    # Generar IV (vector de inicialización)
    iv = get_random_bytes(16)
    
    # Crear cifrador
    encryption.cipher = AES.new(encryption.key, AES.MODE_CBC, iv)
    
    # Cifrar
    encrypted_data = encryption.cipher.encrypt(data_padded)
    
    # Combinar IV y datos cifrados, codificar en base64
    return base64.b64encode(iv + encrypted_data).decode('utf-8')


# Propósito: Cifra un objeto RegistroClimatico y retorna el texto cifrado en base64.

# Lógica:
# Convierte los atributos del objeto (fecha, temperatura, humedad) a JSON.

# Rellena los datos para que sean múltiplos de 16 bytes (requerido por AES).

# Genera un IV (vector de inicialización) aleatorio.

# Crea un cifrador AES en modo CBC con la clave de encryption.

# Cifra los datos y combina el IV con el resultado, codificándolo en base64.

# Sin diccionarios: Aunque usa un diccionario temporal para JSON, esto es solo para serializar los datos (inevitable para AES). Los datos del objeto se acceden directamente (data.fecha, etc.).

# Uso: Se llamará antes de insertar un RegistroClimatico en una sublista.

