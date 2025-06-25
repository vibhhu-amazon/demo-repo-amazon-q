"""
Calculator module providing basic arithmetic operations.
"""

class Calculator:
    """
    A simple calculator class that provides basic arithmetic operations.
    """
    
    def add(self, a, b):
        """
        Add two numbers and return the result.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            The sum of a and b
        """
        return a + b
    
    def subtract(self, a, b):
        """
        Subtract b from a and return the result.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            The difference of a and b (a - b)
        """
        return a - b
    
    def multiply(self, a, b):
        """
        Multiply two numbers and return the result.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            The product of a and b
        """
        return a * b
    
    def divide(self, a, b):
        """
        Divide a by b and return the result.
        
        Args:
            a: First number (dividend)
            b: Second number (divisor)
            
        Returns:
            The quotient of a and b (a / b)
            
        Raises:
            ValueError: If b is zero (division by zero)
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def power(self, a, b):
        """
        Raise a to the power of b and return the result.
        
        Args:
            a: Base number
            b: Exponent
            
        Returns:
            a raised to the power of b
        """
        return a ** b
    
    def square_root(self, a):
        """
        Calculate the square root of a number.
        
        Args:
            a: The number to calculate the square root of
            
        Returns:
            The square root of a
            
        Raises:
            ValueError: If a is negative
        """
        if a < 0:
            raise ValueError("Cannot calculate square root of a negative number")
        return a ** 0.5