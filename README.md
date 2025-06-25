# Calculator Application

A simple calculator application that provides basic arithmetic operations.

## Features

- Basic arithmetic operations (addition, subtraction, multiplication, division)
- Advanced operations (power, square root)
- Command-line interface
- Comprehensive error handling

## Usage

You can use the calculator through the command-line interface:

```bash
# Addition
python main.py add 5 3

# Subtraction
python main.py subtract 10 4

# Multiplication
python main.py multiply 6 7

# Division
python main.py divide 20 5

# Power
python main.py power 2 3

# Square root
python main.py sqrt 16
```

## Running Tests

To run the unit tests:

```bash
python -m unittest discover tests
```

## Project Structure

- `calculator.py`: Contains the Calculator class with all arithmetic operations
- `main.py`: Command-line interface for the calculator
- `tests/`: Directory containing unit tests
  - `test_calculator.py`: Unit tests for the Calculator class
