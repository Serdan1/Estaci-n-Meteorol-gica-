from ..classes.lista import Lista
from ..classes.registro_climatico import RegistroClimatico
from ..classes.encryption import Encryption
from .encrypt_decrypt import decrypt

def barrido(lista, encryption=None):
    """Recorre la lista mostrando sus valores, descifrando registros si es necesario."""
    if not isinstance(lista, Lista):
        raise ValueError("El primer argumento debe ser una Lista")
    
    aux = lista.inicio
    while aux:
        print(str(aux.info))
        if aux.sublista:
            print("  Registros:")
            nodo = aux.sublista.inicio
            while nodo:
                if isinstance(nodo.info, str):
                    try:
                        decrypted_data = decrypt(encryption, nodo.info)
                        registro = RegistroClimatico(
                            decrypted_data['fecha'],
                            decrypted_data['temperatura'],
                            decrypted_data['humedad']
                        )
                        print(f"    {registro}")
                    except Exception as e:
                        print(f"    Error al descifrar: {e}")
                else:
                    print(f"    {nodo.info}")
                nodo = nodo.sig
        aux = aux.sig
        

# Propósito: Recorre la lista e imprime cada elemento, incluyendo los registros en las sublistas (si existen).

# Lógica:
# Itera sobre los nodos, usando el método __str__ de los objetos (Estacion o RegistroClimatico).

# Si un nodo tiene una sublista (como en estaciones), la recorre recursivamente.

# Uso: Muestra la estructura de lista de listas (estaciones con sus registros), ideal para pruebas en consola.

# Se han hecho los siguientes cambios:

# Añadimos un parámetro encryption (opcional) para pasar la instancia de Encryption.

# En las sublistas, verificamos si el info es un string (texto cifrado en base64). Si es así, lo desciframos con decrypt y creamos un RegistroClimatico con los datos descifrados.

# Si el info no está cifrado (por compatibilidad con pruebas anteriores), lo mostramos directamente.

# Lógica:
# Recorre la lista principal e imprime cada estación.

# Para las sublistas, descifra los registros y los muestra como objetos RegistroClimatico.

# Sin diccionarios: Solo usa un diccionario temporal en decrypt (inevitable para JSON), pero los datos se acceden directamente.

# Uso: Permite mostrar registros cifrados en las sublistas de forma legible.

