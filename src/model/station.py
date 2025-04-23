class Estacion:
    """Clase que representa una estación meteorológica."""
    def __init__(self, id_estacion, nombre, ubicacion):
        self.id_estacion = id_estacion  # Identificador único (string o int)
        self.nombre = nombre            # Nombre de la estación
        self.ubicacion = ubicacion     # Ubicación geográfica (ej. "Buenos Aires")

    def __str__(self):
        return f"Estación {self.nombre} (ID: {self.id_estacion}, Ubicación: {self.ubicacion})"


class RegistroClimatico:
    """Clase que representa un registro climático."""
    def __init__(self, fecha, temperatura, humedad):
        self.fecha = fecha             # Fecha del registro (ej. "2025-04-23 10:00")
        self.temperatura = temperatura # Temperatura en °C
        self.humedad = humedad         # Humedad en %

    def __str__(self):
        return f"Fecha: {self.fecha}, Temp: {self.temperatura}°C, Hum: {self.humedad}%"