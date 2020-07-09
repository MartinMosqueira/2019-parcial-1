import unittest
from exadecimal import exadecimal_f

class Test_Exadecimal(unittest.TestCase):
    def test_exadecimal_number_1(self):
        resultado=exadecimal_f(5)
        self.assertEqual(resultado,'5')
    
    def test_exadecimal_number_2(self):
        resultado=exadecimal_f(1700)
        self.assertEqual(resultado,'6A4')
    
    def test_exadecimal_number_3(self):
        resultado=exadecimal_f(2300)
        self.assertEqual(resultado,'8FC')

    def test_exadecimal_number_4(self):
        resultado=exadecimal_f(999)
        self.assertEqual(resultado,'3E7')

    def test_exadecimal_number_5(self):
        resultado=exadecimal_f(9)
        self.assertEqual(resultado,'9')

    def test_exadecimal_number_6(self):
        resultado=exadecimal_f(56)
        self.assertEqual(resultado,'38')

    def test_exadecimal_number_7(self):
        resultado=exadecimal_f(495)
        self.assertEqual(resultado,'1EF')

    def test_exadecimal_number_8(self):
        resultado=exadecimal_f(13)
        self.assertEqual(resultado,'D')

    def test_exadecimal_number_9(self):
        resultado=exadecimal_f(0)
        self.assertEqual(resultado,'0')        

if __name__ == '__main__':
    unittest.main()
