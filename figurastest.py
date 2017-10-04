import unittest
from figuras import Figuras


class FigurasTest(unittest.TestCase):
    def setUp(self):
        self.figuras = Figuras()

    def test_area_cuadrado_lado_4(self):
        self.assertEqual(self.figuras.obtener_area_cuadrado(4), 16)

    def test_area_cuadrado_lado_6(self):
        self.assertEqual(self.figuras.obtener_area_cuadrado(6), 36)

    def test_area_circulo_radio_4(self):
        self.assertEqual(self.figuras.obtener_area_circulo(4), 50.2656)

    def test_area_circulo_radio_6(self):
        self.assertEqual(self.figuras.obtener_area_circulo(6), 113.0976)

    def test_area_rectangulo_base4_altura6(self):
        self.assertEqual(self.figuras.obtener_area_rectangulo(4, 6), 24)

    def test_area_rectangulo_base10_altura7(self):
        self.assertEqual(self.figuras.obtener_area_rectangulo(10, 7), 70)

    def test_area_trapecio_basem5_baseM10_altura10(self):
        self.assertEqual(self.figuras.obtener_area_trapecio(5, 10, 10), 75)

    def test_area_trapecio_basem10_baseM100_altura5(self):
        self.assertEqual(self.figuras.obtener_area_trapecio(10, 100, 5), 275)

    def tearDown(self):
        pass


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
