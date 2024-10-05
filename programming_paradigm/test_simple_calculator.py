import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calc = SimpleCalculator()
    
    # Test the addition method
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)  
        self.assertEqual(self.calc.add(-1, 1), 0)  
        self.assertEqual(self.calc.add(0, 0), 0) 
        self.assertEqual(self.calc.add(-5, -10), -15)
    
    # Test the subtraction method
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)  
        self.assertEqual(self.calc.subtract(0, 0), 0)  
        self.assertEqual(self.calc.subtract(-5, -10), 5)  
        self.assertEqual(self.calc.subtract(100, 50), 50)  
    
    # Test the multiplication method
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(3, 5), 15)  
        self.assertEqual(self.calc.multiply(0, 10), 0)  
        self.assertEqual(self.calc.multiply(-2, 3), -6)  
        self.assertEqual(self.calc.multiply(-4, -5), 20) 
    
    # Test the division method
    def test_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5) 
        self.assertEqual(self.calc.divide(5, -1), -5)  
        self.assertIsNone(self.calc.divide(5, 0))  
        self.assertEqual(self.calc.divide(0, 1), 0)  
        self.assertEqual(self.calc.divide(10, 1), 10)  
    
if __name__ == '__main__':
    unittest.main()
