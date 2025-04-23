from ..classes.nodo_lista import NodoLista
from ..classes.lista import Lista
from ..classes.estacion import Estacion
from .lista_comparar import comparar

def insertar(lista, dato, campo=None):
    """Inserta un dato en la lista de forma ordenada."""
    if not isinstance(lista, Lista):
        raise ValueError("El primer argumento debe ser una Lista")
    
    nodo = NodoLista()
    nodo.info = dato
    if isinstance(dato, Estacion):
        nodo.sublista = Lista()  # Inicializa sublista para estaciones

    if lista.inicio is None or comparar(lista.inicio.info, dato, campo) > 0:
        nodo.sig = lista.inicio
        lista.inicio = nodo
    else:
        ant, act = lista.inicio, lista.inicio.sig
        while act and comparar(act.info, dato, campo) < 0:
            ant, act = act, act.sig
        nodo.sig = act
        ant.sig = nodo
    lista.tamanio += 1


# Propósito: Inserta un elemento (Estacion o RegistroClimatico) en la lista, ordenado por el campo especificado (ej. id_estacion para estaciones, fecha para registros).

# Lógica: 
# Crea un nuevo NodoLista con el dato.

# Si el dato es una Estacion, inicializa su sublista como una nueva Lista.

# Inserta al inicio si la lista está vacía o el dato es menor que el primero.

# Si no, recorre la lista para encontrar la posición correcta.

# Dependencias: Usa comparar para determinar el orden.

