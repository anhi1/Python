import unittest

def suma(a: int | float, b: int | float) -> int | float:
    return a + b

class TestSuma(unittest.TestCase):

    def test_suma_positivos(self):
        self.assertEqual(suma(2,3), 5, "la suma deberia ser 5")

    def test_suma_negativos(self):
        self.assertEqual(suma(-1, 1), 0, "la suma de -1 y 1 no deberia ser 0")

# esto es un bucle de eventos   
if __name__ == '__main__':
    unittest.main()



 # run en la terminal: python -m unittest test1.py