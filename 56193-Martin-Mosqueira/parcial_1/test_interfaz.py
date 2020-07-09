import unittest
from interfaz import funcion

class Test_Interfaz(unittest.TestCase):
    def test_interfaz_number_1(self):
        resultado=funcion('dato')
        self.assertEqual(resultado,'Disculpe,solo acepto numeros enteros')

    def test_interfaz_number_2(self):
        resultado=funcion('%?')
        self.assertEqual(resultado,'Disculpe,solo acepto numeros enteros')

    def test_interfaz_number_3(self):
        resultado=funcion(123)
        self.assertEqual(resultado,'7B')

if __name__ == '__main__':
    unittest.main()