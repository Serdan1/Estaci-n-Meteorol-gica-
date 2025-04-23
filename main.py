from src.model.classes.estacion import Estacion
from src.model.classes.registro_climatico import RegistroClimatico
from src.model.classes.lista import Lista
from src.model.functions.lista_insertar import insertar
from src.model.functions.lista_buscar import buscar
from src.model.functions.lista_eliminar import eliminar
from src.model.functions.lista_barrido import barrido

def main():
    """Función principal para probar la lista de listas."""
    # Crear una lista principal para estaciones
    estaciones = Lista()

    # Crear estaciones de ejemplo
    estacion1 = Estacion("E001", "Buenos Aires", "34.6S, 58.4W")
    estacion2 = Estacion("E002", "Córdoba", "31.4S, 64.2W")

    # Insertar estaciones
    print("Insertando estaciones...")
    insertar(estaciones, estacion1, campo='id_estacion')
    insertar(estaciones, estacion2, campo='id_estacion')

    # Mostrar contenido
    print("\nContenido de la lista:")
    barrido(estaciones)

    # Buscar una estación y añadir un registro
    print("\nBuscando estación E001...")
    nodo = buscar(estaciones, "E001", campo='id_estacion')
    if nodo:
        print(f"Estación encontrada: {nodo.info}")
        registro = RegistroClimatico("2025-04-23 10:00", 25.5, 60)
        insertar(nodo.sublista, registro, campo='fecha')
        print("Añadido registro climático a E001")
    else:
        print("Estación no encontrada")

    # Mostrar contenido con registros
    print("\nContenido de la lista con registros:")
    barrido(estaciones)

    # Eliminar una estación
    print("\nEliminando estación E002...")
    eliminado = eliminar(estaciones, "E002", campo='id_estacion')
    if eliminado:
        print(f"Estación eliminada: {eliminado}")
    else:
        print("Estación no encontrada")

    # Mostrar contenido final
    print("\nContenido final de la lista:")
    barrido(estaciones)

if __name__ == "__main__":
    main()