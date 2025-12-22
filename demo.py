#!/usr/bin/env python3
"""
Demo script for the Calculator application.
This script demonstrates the calculator's capabilities programmatically.
"""

from calculator import Calculator


def demo_basic_operations():
    """Demonstrate basic arithmetic operations."""
    print("=" * 60)
    print("                CALCULATOR DEMO")
    print("=" * 60)
    
    calc = Calculator()
    
    print("\n1. BASIC OPERATIONS DEMO")
    print("-" * 30)
    
    # Addition
    result = calc.add(15, 25)
    print(f"Addition: 15 + 25 = {result}")
    
    # Subtraction
    result = calc.subtract(50, 18)
    print(f"Subtraction: 50 - 18 = {result}")
    
    # Multiplication
    result = calc.multiply(7, 8)
    print(f"Multiplication: 7 × 8 = {result}")
    
    # Division
    result = calc.divide(100, 4)
    print(f"Division: 100 ÷ 4 = {result}")
    
    # Power
    result = calc.power(2, 10)
    print(f"Power: 2^10 = {result}")


def demo_expression_evaluation():
    """Demonstrate expression evaluation capabilities."""
    print("\n2. EXPRESSION EVALUATION DEMO")
    print("-" * 35)
    
    calc = Calculator()
    
    expressions = [
        "2 + 3 * 4",
        "(5 + 3) * 2",
        "100 / (2 + 3)",
        "2^8 + 1",
        "(10 - 2) / 4 + 3",
        "3.14 * 2^2",
        "((2 + 3) * 4) - 5"
    ]
    
    for expr in expressions:
        try:
            result = calc.evaluate_expression(expr)
            print(f"{expr} = {result}")
        except ValueError as e:
            print(f"{expr} = Error: {e}")


def demo_error_handling():
    """Demonstrate error handling capabilities."""
    print("\n3. ERROR HANDLING DEMO")
    print("-" * 28)
    
    calc = Calculator()
    
    # Division by zero
    try:
        calc.divide(10, 0)
    except ValueError as e:
        print(f"Division by zero: {e}")
    
    # Invalid expression
    try:
        calc.evaluate_expression("2 + ")
    except ValueError as e:
        print(f"Invalid expression '2 + ': {e}")
    
    # Division by zero in expression
    try:
        calc.evaluate_expression("10 / 0")
    except ValueError as e:
        print(f"Expression '10 / 0': {e}")


def demo_advanced_calculations():
    """Demonstrate advanced calculation capabilities."""
    print("\n4. ADVANCED CALCULATIONS DEMO")
    print("-" * 35)
    
    calc = Calculator()
    
    # Scientific calculations
    calculations = [
        ("Area of circle (r=5): π × r²", "3.14159 * 5^2"),
        ("Compound interest: P(1+r)^t", "1000 * (1 + 0.05)^10"),
        ("Quadratic formula part: b² - 4ac", "5^2 - 4*2*3"),
        ("Distance formula: √((x₂-x₁)² + (y₂-y₁)²)", "((5-1)^2 + (3-1)^2)^0.5"),
        ("Percentage calculation: 15% of 200", "200 * 15 / 100")
    ]
    
    for description, expression in calculations:
        try:
            result = calc.evaluate_expression(expression)
            print(f"{description}")
            print(f"  {expression} = {result}")
            print()
        except ValueError as e:
            print(f"{description}: Error - {e}")


def main():
    """Run the complete demo."""
    try:
        demo_basic_operations()
        demo_expression_evaluation()
        demo_error_handling()
        demo_advanced_calculations()
        
        print("=" * 60)
        print("Demo completed! Run 'python calculator.py' to use the interactive calculator.")
        print("=" * 60)
        
    except Exception as e:
        print(f"Demo error: {e}")


if __name__ == "__main__":
    main()