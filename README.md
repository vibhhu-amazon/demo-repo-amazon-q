# Simple Calculator

This repository contains a simple calculator implementation in Python.

## Features

The calculator supports the following operations:
- Addition
- Subtraction
- Multiplication
- Division (with error handling for division by zero)

## Usage

```python
from calculator import Calculator

# Create a calculator instance
calc = Calculator()

# Perform operations
sum_result = calc.add(5, 3)       # 8
diff_result = calc.subtract(10, 4) # 6
prod_result = calc.multiply(6, 7)  # 42
quot_result = calc.divide(20, 5)   # 4.0
```

## Running the Demo

To run the demo:

```
python main.py
```

## Running Tests

To run the unit tests:

```
python -m unittest test_calculator.py
```
