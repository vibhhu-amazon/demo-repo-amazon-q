"""
Unit tests for the Calculator class.

This module contains tests for all calculator operations including
basic arithmetic, exponentiation, and tetration.
"""

import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Test cases for the Calculator class."""
    
    def setUp(self):
        """Set up a Calculator instance for each test."""
        self.calc = Calculator()
    
    def test_add(self):
        """Test the add method."""
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)
    
    def test_subtract(self):
        """Test the subtract method."""
        self.assertEqual(self.calc.subtract(10, 4), 6)
        self.assertEqual(self.calc.subtract(5, 10), -5)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(5.5, 2.5), 3.0)
    
    def test_multiply(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.multiply(6, 7), 42)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0)
    
    def test_divide(self):
        """Test the divide method."""
        self.assertEqual(self.calc.divide(20, 5), 4)
        self.assertEqual(self.calc.divide(7, 2), 3.5)
        self.assertEqual(self.calc.divide(0, 5), 0)
        
        # Test division by zero
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)
    
    def test_exponentiate(self):
        """Test the exponentiate method."""
        self.assertEqual(self.calc.exponentiate(2, 3), 8)
        self.assertEqual(self.calc.exponentiate(5, 0), 1)
        self.assertEqual(self.calc.exponentiate(1, 10), 1)
        self.assertEqual(self.calc.exponentiate(2, 0.5), 1.4142135623730951)  # sqrt(2)
        self.assertEqual(self.calc.exponentiate(9, 0.5), 3.0)  # sqrt(9)
    
    def test_tetrate(self):
        """Test the tetrate method."""
        self.assertEqual(self.calc.tetrate(2, 1), 2)
        self.assertEqual(self.calc.tetrate(2, 2), 4)  # 2^2
        self.assertEqual(self.calc.tetrate(2, 3), 16)  # 2^(2^2) = 2^4 = 16
        self.assertEqual(self.calc.tetrate(2, 4), 65536)  # 2^(2^(2^2)) = 2^16 = 65536
        
        # Test with invalid height
        with self.assertRaises(ValueError):
            self.calc.tetrate(2, 0)
        
        with self.assertRaises(ValueError):
            self.calc.tetrate(2, -1)
        
        with self.assertRaises(ValueError):
            self.calc.tetrate(2, 1.5)


if __name__ == "__main__":
    unittest.main()