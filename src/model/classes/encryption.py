from Crypto.Random import get_random_bytes

class Encryption:
    """Clase para cifrar y descifrar datos usando AES."""
    def __init__(self, key=None):
        # Generar una clave de 16 bytes si no se proporciona
        self.key = key if key else get_random_bytes(16)
        self.cipher = None


# Propósito: Define la clase Encryption para manejar el cifrado AES.

# Atributos:
# key: Clave de 16 bytes para AES (generada aleatoriamente si no se proporciona).

# cipher: Almacenará el objeto cifrador (se inicializará en encrypt y decrypt).

# Dependencias: Usa pycryptodome para generar claves aleatorias.

# Sin diccionarios: Solo usa atributos de la clase.

# Uso: Esta clase se usará para cifrar/descrifrar los datos de RegistroClimatico antes de insertarlos en las sublistas.

