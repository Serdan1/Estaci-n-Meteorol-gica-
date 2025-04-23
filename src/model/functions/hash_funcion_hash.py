def funcion_hash(dato, tamanio_tabla):
    """Calcula la posición usando hash por división."""
    return hash(str(dato)) % tamanio_tabla

# Propósito: Mapea un id_estacion a una posición en la tabla hash usando el método de división (página 69 del documento).

# Lógica:
# Convierte dato (el id_estacion) a string y usa la función hash() de Python para generar un valor numérico.

# Aplica el módulo % tamanio_tabla para asegurar que la posición esté en el rango [0, tamanio_tabla-1].

# Sin diccionarios: Solo realiza operaciones aritméticas.

# Uso: Se llamará para determinar dónde insertar o buscar una estación en la tabla.

# Dependencias: No requiere importar clases, ya que opera con datos primitivos.

