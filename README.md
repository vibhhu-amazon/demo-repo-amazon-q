# Simple Calculator

A Python-based calculator application that supports basic arithmetic operations and expression evaluation.

## Features

- **Basic Operations Mode**: Perform individual arithmetic operations with two numbers
  - Addition (+)
  - Subtraction (-)
  - Multiplication (*)
  - Division (/)
  - Power (**)

- **Expression Evaluation Mode**: Evaluate complete mathematical expressions
  - Supports parentheses for grouping
  - Handles order of operations correctly
  - Supports decimal numbers
  - Power operations using ** or ^

- **Interactive Command-Line Interface**: User-friendly menu system
- **Error Handling**: Comprehensive error handling for invalid inputs and operations
- **Help System**: Built-in help and usage instructions

## Installation

No installation required! Just ensure you have Python 3.x installed on your system.

## Usage

### Running the Calculator

```bash
python calculator.py
```

### Basic Operations Mode

1. Select option 1 from the main menu
2. Choose an operation (1-5)
3. Enter two numbers when prompted
4. View the result

Example:
```
Select operation:
1. Addition (+)
Enter your choice (1-6): 1
Enter first number: 15
Enter second number: 25
Result: 15.0 + 25.0 = 40.0
```

### Expression Evaluation Mode

1. Select option 2 from the main menu
2. Enter a mathematical expression
3. View the result

Examples:
```
Enter expression: 2 + 3 * 4
Result: 2 + 3 * 4 = 14

Enter expression: (5 + 3) / 2
Result: (5 + 3) / 2 = 4.0

Enter expression: 2^3 + 1
Result: 2^3 + 1 = 9
```

## Supported Operations

| Operation | Symbol | Example |
|-----------|--------|---------|
| Addition | + | 5 + 3 = 8 |
| Subtraction | - | 5 - 3 = 2 |
| Multiplication | * | 5 * 3 = 15 |
| Division | / | 6 / 3 = 2 |
| Power | ** or ^ | 2^3 = 8 |
| Parentheses | () | (2 + 3) * 4 = 20 |

## Testing

Run the test suite to verify functionality:

```bash
python test_calculator.py
```

## File Structure

```
/workspace/
├── calculator.py       # Main calculator application
├── test_calculator.py  # Test suite
└── README.md          # This documentation
```

## Error Handling

The calculator handles various error conditions:

- **Division by Zero**: Displays appropriate error message
- **Invalid Input**: Prompts for valid numeric input
- **Invalid Expressions**: Shows error for malformed expressions
- **Invalid Characters**: Rejects expressions with unsupported characters

## Examples

### Basic Calculations
```python
# Using the Calculator class directly
from calculator import Calculator

calc = Calculator()
result = calc.add(10, 5)        # Returns 15
result = calc.divide(10, 3)     # Returns 3.333...
result = calc.power(2, 8)       # Returns 256
```

### Expression Evaluation
```python
calc = Calculator()
result = calc.evaluate_expression("(2 + 3) * 4 - 1")  # Returns 19
result = calc.evaluate_expression("2^10")              # Returns 1024
```

## Requirements

- Python 3.x
- No external dependencies required

## License

This project is open source and available under the MIT License.
