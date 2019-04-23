import unittest
from exadecimal import exadecimal_f

class Test_Exadecimal(unittest.TestCase):
    def test_exadecimal_number(self):
        resultado=exadecimal_f(5)
        self.assertEqual(resultado,5)
    def test_exadecimal_number1(self):
        resultado=exadecimal_f(10)
        self.assertEqual(resultado,"A")
    def test_exadecimal_number2(self):
        resultado=exadecimal_f(15)
        self.assertEqual(resultado,"F")
    def test_exadecimal_number3(self):
        resultado=exadecimal_f(4095)
        self.assertEqual(resultado,"FFF")
    def test_exadecimal_number4(self):
        resultado=exadecimal_f(1234)
        self.assertEqual(resultado,"4D2")

if __name__ == '__main__':
    unittest.main()