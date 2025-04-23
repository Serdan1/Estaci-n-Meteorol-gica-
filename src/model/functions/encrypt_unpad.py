def unpad(data):
    """Elimina el relleno de los datos descifrados."""
    if not isinstance(data, bytes):
        raise ValueError("Los datos deben ser bytes")
    
    padding_length = data[-1]
    return data[:-padding_length]


# Propósito: Elimina el relleno de los datos descifrados para recuperar el contenido original.

# Lógica:
# Lee el último byte (padding_length), que indica cuántos bytes de relleno hay.

# Retorna los datos sin los últimos padding_length bytes.

# Sin diccionarios: Opera directamente con bytes.

# Uso: Se llama en decrypt para limpiar los datos después de descifrarlos.

# Dependencias: Similar a pad, no requiere clases.

