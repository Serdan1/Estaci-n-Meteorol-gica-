class RegistroClimatico:
    """Clase que representa un registro climático."""
    def __init__(self, fecha, temperatura, humedad):
        self.fecha = fecha             # Fecha del registro (ej. "2025-04-23 10:00")
        self.temperatura = temperatura # Temperatura en °C
        self.humedad = humedad         # Humedad en %

    def __str__(self):
        return f"Fecha: {self.fecha}, Temp: {self.temperatura}°C, Hum: {self.humedad}%"
    
# Propósito: Representa un registro climático que se almacenará cifrado en las sublistas de cada estación.

# Uso: Los objetos RegistroClimatico irán en las sublistas de la lista de listas.

# Método __str__: Para mostrar los datos en la interfaz o consola.

