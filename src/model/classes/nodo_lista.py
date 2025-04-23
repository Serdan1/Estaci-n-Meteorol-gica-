class NodoLista:
    """Clase para nodos de la lista."""
    def __init__(self):
        self.info = None  # Almacena Estacion o RegistroClimatico
        self.sig = None   # Siguiente nodo
        self.sublista = None  # Sublista para registros climáticos


# Propósito: Define un nodo para la lista simplemente enlazada, con un campo info (para Estacion o RegistroClimatico), un enlace al siguiente nodo (sig), y un campo sublista (para las sublistas de registros).

# Uso: Usado tanto en la lista principal (estaciones) como en las sublistas (registros).

# Nota: La sublista se inicializará como una Lista cuando se implementen las funciones.

