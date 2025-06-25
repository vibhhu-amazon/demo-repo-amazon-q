# Hello World Package

A simple Python package that implements a "Hello, World!" function.

## Installation

```bash
pip install -e .
```

## Usage

You can use the `hello_world` function in your Python code:

```python
from hello_world.hello import hello_world

message = hello_world()
print(message)  # Outputs: Hello, World!
```

Alternatively, you can run the main script:

```bash
python main.py
```

## Testing

Run the tests with:

```bash
python -m unittest discover tests
```
