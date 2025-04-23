from src.model.classes.estacion import Estacion
from src.model.classes.registro_climatico import RegistroClimatico
from src.model.classes.lista import Lista
from src.model.classes.tabla_hash import TablaHash
from src.model.classes.encryption import Encryption
from src.model.functions.lista_insertar import insertar
from src.model.functions.lista_buscar import buscar
from src.model.functions.lista_eliminar import eliminar
from src.model.functions.lista_barrido import barrido
from src.model.functions.hash_agregar import agregar
from src.model.functions.hash_buscar import buscar as hash_buscar
from src.model.functions.hash_cantidad import cantidad_elementos
from src.model.functions.encrypt_encrypt import encrypt

def main():
    """Función principal para probar la lista de listas y tabla hash con cifrado."""
    # Crear una lista principal para estaciones
    estaciones_lista = Lista()
    
    # Crear una tabla hash (tamaño 9, como en Figura 2)
    estaciones_tabla = TablaHash(9)
    
    # Crear instancia de cifrado
    encryption = Encryption()

    # Crear estaciones de ejemplo
    estacion1 = Estacion("E001", "Buenos Aires", "34.6S, 58.4W")
    estacion2 = Estacion("E002", "Córdoba", "31.4S, 64.2W")

    # Insertar estaciones en la lista y la tabla
    print("Insertando estaciones...")
    insertar(estaciones_lista, estacion1, campo='id_estacion')
    insertar(estaciones_lista, estacion2, campo='id_estacion')
    agregar(estaciones_tabla, estacion1)
    agregar(estaciones_tabla, estacion2)

    # Mostrar contenido de la lista
    print("\nContenido de la lista de listas:")
    barrido(estaciones_lista, encryption)

    # Mostrar cantidad de estaciones en la tabla
    print(f"\nCantidad de estaciones en la tabla hash: {cantidad_elementos(estaciones_tabla)}")

    # Buscar una estación en la tabla
    print("\nBuscando estación E001 en la tabla hash...")
    estacion_encontrada = hash_buscar(estaciones_tabla, "E001")
    if estacion_encontrada:
        print(f"Estación encontrada: {estacion_encontrada}")
    else:
        print("Estación no encontrada")

    # Buscar una estación en la lista y añadir un registro cifrado
    print("\nBuscando estación E001 en la lista...")
    nodo = buscar(estaciones_lista, "E001", campo='id_estacion')
    if nodo:
        print(f"Estación encontrada: {nodo.info}")
        registro = RegistroClimatico("2025-04-23 10:00", 25.5, 60)
        encrypted_registro = encrypt(encryption, registro)
        insertar(nodo.sublista, encrypted_registro, campo=None)
        print("Añadido registro climático cifrado a E001")
    else:
        print("Estación no encontrada")

    # Mostrar contenido con registros
    print("\nContenido de la lista con registros cifrados:")
    barrido(estaciones_lista, encryption)

    # Eliminar una estación
    print("\nEliminando estación E002 de la lista...")
    eliminado = eliminar(estaciones_lista, "E002", campo='id_estacion')
    if eliminado:
        print(f"Estación eliminada: {eliminado}")
    else:
        print("Estación no encontrada")

    # Mostrar contenido final
    print("\nContenido final de la lista:")
    barrido(estaciones_lista, encryption)

if __name__ == "__main__":
    main()

    