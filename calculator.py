#!/usr/bin/env python3
"""
Simple Calculator Application
Supports basic arithmetic operations: addition, subtraction, multiplication, and division.
"""

import sys
import re


class Calculator:
    """A simple calculator class that performs basic arithmetic operations."""
    
    def add(self, a, b):
        """Add two numbers."""
        return a + b
    
    def subtract(self, a, b):
        """Subtract second number from first number."""
        return a - b
    
    def multiply(self, a, b):
        """Multiply two numbers."""
        return a * b
    
    def divide(self, a, b):
        """Divide first number by second number."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def power(self, a, b):
        """Raise first number to the power of second number."""
        return a ** b
    
    def evaluate_expression(self, expression):
        """
        Evaluate a mathematical expression string.
        Supports +, -, *, /, ** operations and parentheses.
        """
        # Remove spaces
        expression = expression.replace(' ', '')
        
        # Basic validation
        if not re.match(r'^[0-9+\-*/().^]+$', expression):
            raise ValueError("Invalid characters in expression")
        
        # Replace ^ with ** for power operations
        expression = expression.replace('^', '**')
        
        try:
            # Use eval with restricted globals for safety
            result = eval(expression, {"__builtins__": {}})
            return result
        except ZeroDivisionError:
            raise ValueError("Cannot divide by zero")
        except Exception as e:
            raise ValueError(f"Invalid expression: {str(e)}")


def print_menu():
    """Print the calculator menu."""
    print("\n" + "="*50)
    print("           SIMPLE CALCULATOR")
    print("="*50)
    print("1. Basic Operations (enter two numbers)")
    print("2. Expression Evaluation (enter full expression)")
    print("3. Help")
    print("4. Exit")
    print("="*50)


def print_operations_menu():
    """Print the basic operations menu."""
    print("\nSelect operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (**)")
    print("6. Back to main menu")


def get_number_input(prompt):
    """Get a valid number input from user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def basic_operations_mode(calc):
    """Handle basic operations mode."""
    while True:
        print_operations_menu()
        
        try:
            choice = input("\nEnter your choice (1-6): ").strip()
            
            if choice == '6':
                break
            
            if choice not in ['1', '2', '3', '4', '5']:
                print("Invalid choice! Please select 1-6.")
                continue
            
            # Get numbers from user
            num1 = get_number_input("Enter first number: ")
            num2 = get_number_input("Enter second number: ")
            
            # Perform operation based on choice
            if choice == '1':
                result = calc.add(num1, num2)
                operation = "+"
            elif choice == '2':
                result = calc.subtract(num1, num2)
                operation = "-"
            elif choice == '3':
                result = calc.multiply(num1, num2)
                operation = "*"
            elif choice == '4':
                result = calc.divide(num1, num2)
                operation = "/"
            elif choice == '5':
                result = calc.power(num1, num2)
                operation = "**"
            
            print(f"\nResult: {num1} {operation} {num2} = {result}")
            
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            break


def expression_mode(calc):
    """Handle expression evaluation mode."""
    print("\nExpression Evaluation Mode")
    print("Enter mathematical expressions (e.g., '2 + 3 * 4', '(5 + 3) / 2')")
    print("Supported operations: +, -, *, /, ** (or ^), parentheses")
    print("Type 'back' to return to main menu")
    
    while True:
        try:
            expression = input("\nEnter expression: ").strip()
            
            if expression.lower() == 'back':
                break
            
            if not expression:
                print("Please enter a valid expression.")
                continue
            
            result = calc.evaluate_expression(expression)
            print(f"Result: {expression} = {result}")
            
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            break


def print_help():
    """Print help information."""
    print("\n" + "="*60)
    print("                        HELP")
    print("="*60)
    print("This calculator supports two modes:")
    print("\n1. Basic Operations Mode:")
    print("   - Choose an operation and enter two numbers")
    print("   - Supports: addition, subtraction, multiplication, division, power")
    print("\n2. Expression Evaluation Mode:")
    print("   - Enter complete mathematical expressions")
    print("   - Examples: '2 + 3', '(5 + 3) * 2', '10 / (2 + 3)'")
    print("   - Supported operators: +, -, *, /, ** (power), ^ (power)")
    print("   - Supports parentheses for grouping")
    print("\nTips:")
    print("- Use parentheses to control order of operations")
    print("- Decimal numbers are supported (e.g., 3.14, 2.5)")
    print("- Division by zero will show an error")
    print("="*60)


def main():
    """Main function to run the calculator."""
    calc = Calculator()
    
    print("Welcome to the Simple Calculator!")
    
    while True:
        try:
            print_menu()
            choice = input("Enter your choice (1-4): ").strip()
            
            if choice == '1':
                basic_operations_mode(calc)
            elif choice == '2':
                expression_mode(calc)
            elif choice == '3':
                print_help()
            elif choice == '4':
                print("\nThank you for using the calculator! Goodbye!")
                sys.exit(0)
            else:
                print("Invalid choice! Please select 1-4.")
                
        except KeyboardInterrupt:
            print("\n\nThank you for using the calculator! Goodbye!")
            sys.exit(0)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()