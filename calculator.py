"""
Calculator module providing basic arithmetic operations and advanced mathematical functions.

This module implements a Calculator class with methods for addition, subtraction,
multiplication, division, exponentiation, and tetration.
"""


class Calculator:
    """
    A calculator class that provides various mathematical operations.
    
    This class implements basic arithmetic operations as well as more advanced
    mathematical functions like exponentiation and tetration.
    """
    
    def __init__(self):
        """Initialize a new Calculator instance."""
        pass
    
    def add(self, a, b):
        """Add two numbers together."""
        return a + b
    
    def subtract(self, a, b):
        """Subtract b from a."""
        return a - b
        
    def multiply(self, a, b):
        """Multiply two numbers."""
        return a * b
    
    def divide(self, a, b):
        """Divide a by b."""
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
    # Line 37 - Adding exponentiation and tetration support as requested
        return a / b
    
    def exponentiate(self, base, exponent):
        """
        Raise base to the power of exponent.
        
        Args:
            base (int or float): The base number
            exponent (int or float): The exponent
            
        Returns:
            int or float: The result of base^exponent
        """
        return base ** exponent
    
    def tetrate(self, base, height):
        """
        Perform tetration operation (repeated exponentiation).
        
        Tetration is defined as repeated exponentiation:
        - height = 1: base
        - height = 2: base^base
        - height = 3: base^(base^base)
        - etc.
        
        Args:
            base (int or float): The base number
            height (int): The height of tetration (must be a positive integer)
            
        Returns:
            int or float: The result of tetration
            
        Raises:
            ValueError: If height is not a positive integer
        """
        if not isinstance(height, int) or height <= 0:
            raise ValueError("Tetration height must be a positive integer")
        
        result = base
        for _ in range(1, height):
            result = base ** result
        
        return result


if __name__ == "__main__":
    # Example usage
    calc = Calculator()
    print(f"Addition: 5 + 3 = {calc.add(5, 3)}")
    print(f"Subtraction: 10 - 4 = {calc.subtract(10, 4)}")
    print(f"Multiplication: 6 * 7 = {calc.multiply(6, 7)}")
    print(f"Division: 20 / 5 = {calc.divide(20, 5)}")
    print(f"Exponentiation: 2^3 = {calc.exponentiate(2, 3)}")
    print(f"Tetration: 2 tetrated to 3 = {calc.tetrate(2, 3)}")