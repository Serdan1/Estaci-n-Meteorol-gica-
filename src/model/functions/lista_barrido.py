from ..classes.lista import Lista

def barrido(lista):
    """Recorre la lista mostrando sus valores."""
    if not isinstance(lista, Lista):
        raise ValueError("El primer argumento debe ser una Lista")
    
    aux = lista.inicio
    while aux:
        print(str(aux.info))
        if aux.sublista:
            print("  Registros:")
            barrido(aux.sublista)  # Recursivo para sublistas
        aux = aux.sig

# Propósito: Recorre la lista e imprime cada elemento, incluyendo los registros en las sublistas (si existen).

# Lógica:
# Itera sobre los nodos, usando el método __str__ de los objetos (Estacion o RegistroClimatico).

# Si un nodo tiene una sublista (como en estaciones), la recorre recursivamente.

# Uso: Muestra la estructura de lista de listas (estaciones con sus registros), ideal para pruebas en consola.

