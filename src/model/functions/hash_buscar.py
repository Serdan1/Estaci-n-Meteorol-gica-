from ..classes.tabla_hash import TablaHash
from ..functions.lista_buscar import buscar
from .hash_funcion_hash import funcion_hash

def buscar(tabla, id_estacion):
    """Busca una estación por su id_estacion."""
    if not isinstance(tabla, TablaHash):
        raise ValueError("El primer argumento debe ser una TablaHash")
    
    posicion = funcion_hash(id_estacion, tabla.tamanio)
    if tabla.tabla[posicion] is not None:
        nodo = buscar(tabla.tabla[posicion], id_estacion, campo='id_estacion')
        return nodo.info if nodo else None
    return None

# Propósito: Busca una estación en la tabla hash por su id_estacion, retornando el objeto Estacion o None.

# Lógica:
# Calcula la posición con funcion_hash.

# Si la posición no está vacía, busca en la lista de esa posición usando buscar.

# Retorna la estación encontrada o None si no existe.

# Sin diccionarios: Opera con el arreglo y listas enlazadas.

# Dependencias: Importa TablaHash, buscar, y funcion_hash.

# Uso: Permite localizar estaciones rápidamente, cumpliendo el objetivo de la tabla hash (Figura 1).

