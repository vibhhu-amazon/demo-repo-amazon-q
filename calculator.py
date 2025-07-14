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
            ZeroDivisionError: If b is zero
        """
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b