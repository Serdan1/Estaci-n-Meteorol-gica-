import unittest
from src.model.classes.lista import Lista
from src.model.classes.estacion import Estacion
from src.model.classes.registro_climatico import RegistroClimatico
from src.model.functions.lista_insertar import insertar
from src.model.functions.lista_buscar import buscar as lista_buscar
from src.model.functions.lista_eliminar import eliminar

class TestLista(unittest.TestCase):
    def setUp(self):
        self.lista = Lista()

    def test_insertar_y_buscar(self):
        estacion = Estacion("E001", "Buenos Aires", "34.6S, 58.4W")
        insertar(self.lista, estacion, campo='id_estacion')
        nodo = lista_buscar(self.lista, "E001", campo='id_estacion')
        self.assertIsNotNone(nodo)
        self.assertEqual(nodo.info.id_estacion, "E001")

    def test_eliminar(self):
        estacion = Estacion("E001", "Buenos Aires", "34.6S, 58.4W")
        insertar(self.lista, estacion, campo='id_estacion')
        eliminado = eliminar(self.lista, "E001", campo='id_estacion')
        self.assertIsNotNone(eliminado)
        self.assertEqual(eliminado.id_estacion, "E001")
        nodo = lista_buscar(self.lista, "E001", campo='id_estacion')
        self.assertIsNone(nodo)

    def test_sublista(self):
        estacion = Estacion("E001", "Buenos Aires", "34.6S, 58.4W")
        insertar(self.lista, estacion, campo='id_estacion')
        nodo = lista_buscar(self.lista, "E001", campo='id_estacion')
        registro = RegistroClimatico("2025-04-23 10:00", 25.5, 60)
        insertar(nodo.sublista, registro, campo='fecha')
        nodo_reg = lista_buscar(nodo.sublista, "2025-04-23 10:00", campo='fecha')
        self.assertIsNotNone(nodo_reg)
        self.assertEqual(nodo_reg.info.fecha, "2025-04-23 10:00")

if __name__ == "__main__":
    unittest.main()
    
# Pruebas:
# test_insertar_y_buscar: Verifica que una estación se inserte y se encuentre correctamente.

# test_eliminar: Verifica que una estación se elimine y ya no se encuentre.

# test_sublista: Verifica que se puedan insertar y buscar registros en una sublista.

# Uso: Asegura que la lista de listas dinámica funcione correctamente.

