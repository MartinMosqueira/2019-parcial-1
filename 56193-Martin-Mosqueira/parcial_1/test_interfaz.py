import unittest
from interfaz import funcion

class Test_Interfaz(unittest.TestCase):
    def test_interfaz_number(self):
        resultado=funcion("hola")
        self.assertEqual(resultado,"Disculpe,solo acepto numeros")

if __name__ == '__main__':
    unittest.main()