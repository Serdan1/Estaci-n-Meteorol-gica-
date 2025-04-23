from ..classes.tabla_hash import TablaHash
from ..classes.estacion import Estacion
from ..classes.lista import Lista
from ..functions.lista_insertar import insertar
from .hash_funcion_hash import funcion_hash

def agregar(tabla, dato):
    """Agrega una estación a la tabla hash."""
    if not isinstance(tabla, TablaHash):
        raise ValueError("El primer argumento debe ser una TablaHash")
    if not isinstance(dato, Estacion):
        raise ValueError("El dato debe ser una Estacion")
    
    posicion = funcion_hash(dato.id_estacion, tabla.tamanio)
    if tabla.tabla[posicion] is None:
        tabla.tabla[posicion] = Lista()
    insertar(tabla.tabla[posicion], dato, campo='id_estacion')
    

# Propósito: Inserta una estación en la tabla hash en la posición determinada por id_estacion.

# Lógica:
# Calcula la posición usando funcion_hash.

# Si la posición está vacía (None), inicializa una nueva Lista.

# Inserta la estación en la lista de esa posición, ordenada por id_estacion usando insertar.

# Sin diccionarios: Usa un arreglo (tabla.tabla) y listas enlazadas.

# Dependencias: Importa TablaHash, Estacion, Lista, insertar, y funcion_hash.

# Uso: Permite añadir estaciones a la tabla hash, manejando colisiones con listas enlazadas.

