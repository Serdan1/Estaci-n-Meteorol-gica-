def pad(data):
    """Rellena los datos para que sean múltiplos de 16 bytes."""
    if not isinstance(data, bytes):
        raise ValueError("Los datos deben ser bytes")
    
    padding_length = 16 - (len(data) % 16)
    return data + (chr(padding_length) * padding_length).encode()

# Propósito: Añade relleno a los datos para que su longitud sea múltiplo de 16 bytes, requerido por AES.

# Lógica:
# Calcula cuántos bytes faltan para el próximo múltiplo de 16 (padding_length).

# Añade padding_length bytes, cada uno con el valor padding_length (estándar PKCS5/PKCS7).

# Sin diccionarios: Solo opera con bytes, sin estructuras adicionales.

# Uso: Se llama en encrypt para preparar los datos antes de cifrarlos.

# Dependencias: No requiere importar clases, ya que opera directamente con bytes.

