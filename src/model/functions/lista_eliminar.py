from ..classes.lista import Lista
from .lista_comparar import comparar

def eliminar(lista, clave, campo=None):
    """Elimina un elemento de la lista y lo devuelve."""
    if not isinstance(lista, Lista):
        raise ValueError("El primer argumento debe ser una Lista")
    
    dato = None
    if lista.inicio and comparar(lista.inicio.info, clave, campo) == 0:
        dato = lista.inicio.info
        lista.inicio = lista.inicio.sig
        lista.tamanio -= 1
    else:
        ant, act = lista.inicio, lista.inicio.sig
        while act and comparar(act.info, clave, campo) != 0:
            ant, act = act, act.sig
        if act:
            dato = act.info
            ant.sig = act.sig
            lista.tamanio -= 1
    return dato

# Propósito: Elimina el primer elemento de la lista cuya clave coincide con el campo especificado (ej. id_estacion para estaciones, fecha para registros) y lo retorna.

# Lógica:
# Si el elemento está al inicio, actualiza inicio y reduce tamanio.

# Si no, usa dos punteros (ant y act) para encontrar y eliminar el nodo.

# Retorna None si no se encuentra el elemento.

# Dependencias: Usa comparar para verificar coincidencias.

# Uso: Por ejemplo, eliminar una estación por id_estacion o un registro por fecha

