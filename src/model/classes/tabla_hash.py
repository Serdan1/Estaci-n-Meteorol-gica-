class TablaHash:
    """Clase para tabla hash encadenada."""
    def __init__(self, tamanio):
        self.tabla = [None] * tamanio  # Arreglo de listas
        self.tamanio = tamanio         # Tamaño de la tabla

# Propósito: Define una tabla hash encadenada, donde cada posición del arreglo tabla puede contener una Lista (para manejar colisiones).

# Atributos:
# tabla: Arreglo de tamaño fijo inicializado con None.

# tamanio: Tamaño del arreglo, usado para la función hash.

# Sin diccionarios: Usa un arreglo simple, cumpliendo el requisito.

# Uso: Almacenará objetos Estacion, accediendo a ellos por id_estacion.

# Dependencias: No requiere imports aún, pero usará Lista en funciones como agregar.

