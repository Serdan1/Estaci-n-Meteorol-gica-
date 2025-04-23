from ..classes.estacion import Estacion
from ..classes.registro_climatico import RegistroClimatico
from .lista_obtener_valor import obtener_valor

def comparar(info1, info2, campo=None):
    """Compara dos elementos según el campo especificado."""
    val1 = obtener_valor(info1, campo)
    val2 = obtener_valor(info2, campo)
    if val1 < val2:
        return -1
    elif val1 > val2:
        return 1
    return 0


# Propósito: Compara dos elementos (info1 y info2) según el campo especificado, retornando -1 (menor), 0 (igual), o 1 (mayor).

# Lógica: Obtiene los valores con obtener_valor y los compara.

# Dependencias: Usa obtener_valor para acceder a los atributos.

