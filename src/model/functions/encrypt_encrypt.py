from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import json
from ..classes.encryption import Encryption
from .encrypt_pad import pad

def encrypt(encryption, data):
    """Cifra un objeto y devuelve el texto cifrado en base64."""
    if not isinstance(encryption, Encryption):
        raise ValueError("El primer argumento debe ser una Encryption")
    
    data_json = json.dumps({
        'fecha': data.fecha,
        'temperatura': data.temperatura,
        'humedad': data.humedad
    }).encode()
    
    data_padded = pad(data_json)
    
    iv = get_random_bytes(16)
    
    encryption.cipher = AES.new(encryption.key, AES.MODE_CBC, iv)
    
    encrypted_data = encryption.cipher.encrypt(data_padded)
    
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

