from ..classes.tabla_hash import TablaHash

def cantidad_elementos(tabla):
    """Devuelve la cantidad de elementos en la tabla hash."""
    if not isinstance(tabla, TablaHash):
        raise ValueError("El primer argumento debe ser una TablaHash")
    
    total = 0
    for lista in tabla.tabla:
        if lista is not None:
            total += lista.tamanio
    return total

# Propósito: Cuenta el número total de estaciones almacenadas en la tabla hash.

# Lógica:
# Itera sobre el arreglo tabla.tabla.

# Para cada posición no vacía, suma el tamanio de la lista enlazada en esa posición.

# Sin diccionarios: Usa el arreglo tabla.tabla y el atributo tamanio de las listas.

# Dependencias: Solo importa TablaHash, ya que accede al atributo tamanio de las instancias de Lista.

# Uso: Proporciona una forma de verificar cuántas estaciones están en la tabla hash, útil para pruebas y depuración.

