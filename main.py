"""
Main script demonstrating the use of the Calculator class.
"""

from calculator import Calculator

def main():
    """
    Demonstrate the use of the Calculator class.
    """
    calc = Calculator()
    
    # Addition
    result = calc.add(5, 3)
    print(f"5 + 3 = {result}")
    
    # Subtraction
    result = calc.subtract(10, 4)
    print(f"10 - 4 = {result}")
    
    # Multiplication
    result = calc.multiply(6, 7)
    print(f"6 * 7 = {result}")
    
    # Division
    result = calc.divide(20, 5)
    print(f"20 / 5 = {result}")
    
    # Division by zero (will raise an exception)
    try:
        result = calc.divide(10, 0)
    except ZeroDivisionError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()