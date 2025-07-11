# Hello World Python Project

This simple Python project provides a "Hello, World!" function.

## Installation

You can install this package directly from the repository:

```bash
pip install git+https://github.com/vibhhu-amazon/demo-repo-amazon-q.git
```

Or for development:

```bash
git clone https://github.com/vibhhu-amazon/demo-repo-amazon-q.git
cd demo-repo-amazon-q
pip install -e .
```

## Requirements

- Python 3.6 or higher

## Usage

You can use the `hello_world` function in your Python code:

```python
from hello_world import hello_world

# Get the hello world message
message = hello_world()
print(message)  # Outputs: Hello, World!
```

Alternatively, you can run the module directly:

```bash
python -m hello_world.hello_world
```

## Testing

To run the tests:

```bash
python -m unittest discover tests
```
