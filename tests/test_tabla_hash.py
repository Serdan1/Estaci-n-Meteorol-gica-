import unittest
from src.model.classes.tabla_hash import TablaHash
from src.model.classes.estacion import Estacion
from src.model.functions.hash_agregar import agregar
from src.model.functions.hash_buscar import buscar as hash_buscar
from src.model.functions.hash_cantidad import cantidad_elementos

class TestTablaHash(unittest.TestCase):
    def setUp(self):
        self.tabla = TablaHash(9)

    def test_agregar_y_buscar(self):
        estacion = Estacion("E001", "Buenos Aires", "34.6S, 58.4W")
        agregar(self.tabla, estacion)
        encontrada = hash_buscar(self.tabla, "E001")
        self.assertIsNotNone(encontrada)
        self.assertEqual(encontrada.id_estacion, "E001")

    def test_cantidad_elementos(self):
        estacion1 = Estacion("E001", "Buenos Aires", "34.6S, 58.4W")
        estacion2 = Estacion("E002", "Córdoba", "31.4S, 64.2W")
        agregar(self.tabla, estacion1)
        agregar(self.tabla, estacion2)
        self.assertEqual(cantidad_elementos(self.tabla), 2)

if __name__ == "__main__":
    unittest.main()

# Pruebas:
# test_agregar_y_buscar: Verifica que una estación se inserte y se encuentre en la tabla hash.

# test_cantidad_elementos: Verifica que la tabla hash cuente correctamente el número de estaciones.

# Uso: Asegura que la tabla hash funcione correctamente.

