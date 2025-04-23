from ..classes.lista import Lista
from .lista_comparar import comparar

def buscar(lista, buscado, campo=None):
    """Busca un elemento en la lista."""
    if not isinstance(lista, Lista):
        raise ValueError("El primer argumento debe ser una Lista")
    
    aux = lista.inicio
    while aux and comparar(aux.info, buscado, campo) != 0:
        aux = aux.sig
    return aux


# Propósito: Busca un elemento en la lista por su valor en el campo especificado, retornando el nodo correspondiente o None.

# Lógica: Recorre la lista comparando cada elemento con buscado hasta encontrarlo o llegar al final.

# Dependencias: Usa comparar para la comparación.

# Uso: Por ejemplo, buscar una estación por id_estacion o un registro por fecha.

