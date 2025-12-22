#!/usr/bin/env python3
"""
Test suite for the Calculator application.
Run this file to test the calculator functionality.
"""

import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Test cases for the Calculator class."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.calc = Calculator()
    
    def test_addition(self):
        """Test addition operation."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(2.5, 3.7), 6.2)
    
    def test_subtraction(self):
        """Test subtraction operation."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(1, 1), 0)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(7.5, 2.3), 5.2)
    
    def test_multiplication(self):
        """Test multiplication operation."""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)
    
    def test_division(self):
        """Test division operation."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(7, 2), 3.5)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertEqual(self.calc.divide(0, 5), 0)
    
    def test_division_by_zero(self):
        """Test division by zero raises ValueError."""
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)
    
    def test_power(self):
        """Test power operation."""
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 0), 1)
        self.assertEqual(self.calc.power(4, 0.5), 2.0)
        self.assertEqual(self.calc.power(-2, 2), 4)
    
    def test_expression_evaluation(self):
        """Test expression evaluation."""
        self.assertEqual(self.calc.evaluate_expression("2 + 3"), 5)
        self.assertEqual(self.calc.evaluate_expression("10 - 4"), 6)
        self.assertEqual(self.calc.evaluate_expression("3 * 4"), 12)
        self.assertEqual(self.calc.evaluate_expression("15 / 3"), 5)
        self.assertEqual(self.calc.evaluate_expression("2 ** 3"), 8)
        self.assertEqual(self.calc.evaluate_expression("2 ^ 3"), 8)  # ^ should work as **
    
    def test_complex_expressions(self):
        """Test complex mathematical expressions."""
        self.assertEqual(self.calc.evaluate_expression("(2 + 3) * 4"), 20)
        self.assertEqual(self.calc.evaluate_expression("10 / (2 + 3)"), 2)
        self.assertEqual(self.calc.evaluate_expression("2 + 3 * 4"), 14)
        self.assertEqual(self.calc.evaluate_expression("(5 + 3) / 2"), 4)
    
    def test_invalid_expressions(self):
        """Test that invalid expressions raise ValueError."""
        with self.assertRaises(ValueError):
            self.calc.evaluate_expression("2 + ")
        
        with self.assertRaises(ValueError):
            self.calc.evaluate_expression("2 / 0")
        
        with self.assertRaises(ValueError):
            self.calc.evaluate_expression("2 + abc")


def run_tests():
    """Run all tests and display results."""
    print("Running Calculator Tests...")
    print("=" * 50)
    
    # Create test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculator)
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "=" * 50)
    if result.wasSuccessful():
        print("All tests passed! ✅")
    else:
        print(f"Tests failed: {len(result.failures)} failures, {len(result.errors)} errors ❌")
    
    return result.wasSuccessful()


if __name__ == "__main__":
    run_tests()