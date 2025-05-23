from Crypto.Cipher import AES
import base64
import json
from ..classes.encryption import Encryption
from .encrypt_unpad import unpad

def decrypt(encryption, encrypted_data):
    """Descifra un texto cifrado en base64 y devuelve el objeto original."""
    if not isinstance(encryption, Encryption):
        raise ValueError("El primer argumento debe ser una Encryption")
    
    raw = base64.b64decode(encrypted_data)
    
    iv, encrypted_data = raw[:16], raw[16:]
    
    encryption.cipher = AES.new(encryption.key, AES.MODE_CBC, iv)
    
    decrypted_padded = encryption.cipher.decrypt(encrypted_data)
    
    decrypted_data = unpad(decrypted_padded)
    
    data_dict = json.loads(decrypted_data.decode())
    return {
        'fecha': data_dict['fecha'],
        'temperatura': data_dict['temperatura'],
        'humedad': data_dict['humedad']
    }


# Propósito: Descifra un texto cifrado en base64 y retorna los datos originales como un diccionario (que luego se convertirá a RegistroClimatico).

# Lógica:
# Decodifica el texto base64.

# Separa el IV y los datos cifrados.

# Crea un cifrador AES con la misma clave y el IV.

# Descifra los datos, elimina el relleno, y convierte el JSON a un diccionario.

# Sin diccionarios: Similar a encrypt, usa un diccionario temporal para JSON, pero los datos finales son accesibles sin diccionarios.

# Uso: Se usará para recuperar los datos de los registros al mostrarlos en la interfaz o consola.

