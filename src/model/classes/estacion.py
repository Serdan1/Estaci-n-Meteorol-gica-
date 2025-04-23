class Estacion:
    """Clase que representa una estación meteorológica."""
    def __init__(self, id_estacion, nombre, ubicacion):
        self.id_estacion = id_estacion  # Identificador único (string o int)
        self.nombre = nombre            # Nombre de la estación
        self.ubicacion = ubicacion     # Ubicación geográfica (ej. "Buenos Aires")

    def __str__(self):
        return f"Estación {self.nombre} (ID: {self.id_estacion}, Ubicación: {self.ubicacion})"
    
# Propósito: Modela una estación meteorológica con un id_estacion único (para la tabla hash), un nombre, y una ubicación.

# Uso: Los objetos Estacion se almacenarán en la lista principal de la lista de listas.

# Método __str__: Facilita la visualización en consola o en la interfaz Gradio.

