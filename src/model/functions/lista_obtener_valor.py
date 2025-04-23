from ..classes.estacion import Estacion
from ..classes.registro_climatico import RegistroClimatico

def obtener_valor(info, campo):
    """Obtiene el valor de un campo sin usar diccionarios."""
    if campo is None:
        return info
    if isinstance(info, Estacion):
        if campo == 'id_estacion':
            return info.id_estacion
        elif campo == 'nombre':
            return info.nombre
        elif campo == 'ubicacion':
            return info.ubicacion
    elif isinstance(info, RegistroClimatico):
        if campo == 'fecha':
            return info.fecha
        elif campo == 'temperatura':
            return info.temperatura
        elif campo == 'humedad':
            return info.humedad
    return info

# Propósito: Obtiene el valor de un campo específico de un objeto (Estacion o RegistroClimatico) sin usar diccionarios.

# Lógica: Verifica el tipo de objeto y el campo, retornando el atributo correspondiente.

# Sin diccionarios: Accede directamente a los atributos (info.id_estacion, etc.), cumpliendo el requisito.

# Flexibilidad: Maneja casos donde campo es None, retornando el objeto completo.

