#!/usr/bin/env python3
"""
Command-line interface for the calculator application.
"""

import sys
from calculator import Calculator

def display_help():
    """Display help information for the calculator."""
    print("Calculator Application")
    print("Usage: python main.py <operation> <number1> <number2>")
    print("\nAvailable operations:")
    print("  add        - Add two numbers")
    print("  subtract   - Subtract second number from first")
    print("  multiply   - Multiply two numbers")
    print("  divide     - Divide first number by second")
    print("  power      - Raise first number to the power of second")
    print("  sqrt       - Calculate square root of a number (only requires one number)")
    print("\nExamples:")
    print("  python main.py add 5 3")
    print("  python main.py divide 10 2")
    print("  python main.py sqrt 16")

def main():
    """Main entry point for the calculator application."""
    if len(sys.argv) < 2 or sys.argv[1] in ['-h', '--help']:
        display_help()
        return
    
    calculator = Calculator()
    operation = sys.argv[1].lower()
    
    try:
        if operation == 'sqrt':
            if len(sys.argv) != 3:
                print("Error: Square root operation requires exactly one number")
                return
            num = float(sys.argv[2])
            result = calculator.square_root(num)
            print(f"Square root of {num} = {result}")
        else:
            if len(sys.argv) != 4:
                print(f"Error: {operation} operation requires exactly two numbers")
                return
            
            num1 = float(sys.argv[2])
            num2 = float(sys.argv[3])
            
            if operation == 'add':
                result = calculator.add(num1, num2)
                print(f"{num1} + {num2} = {result}")
            elif operation == 'subtract':
                result = calculator.subtract(num1, num2)
                print(f"{num1} - {num2} = {result}")
            elif operation == 'multiply':
                result = calculator.multiply(num1, num2)
                print(f"{num1} * {num2} = {result}")
            elif operation == 'divide':
                result = calculator.divide(num1, num2)
                print(f"{num1} / {num2} = {result}")
            elif operation == 'power':
                result = calculator.power(num1, num2)
                print(f"{num1} ^ {num2} = {result}")
            else:
                print(f"Error: Unknown operation '{operation}'")
                display_help()
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()