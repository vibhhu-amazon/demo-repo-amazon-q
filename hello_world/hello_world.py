"""
A simple module that provides a hello world function.
"""

def hello_world() -> str:
    """
    Returns the string "Hello, World!"
    
    Returns:
        str: The greeting string "Hello, World!"
    """
    return "Hello, World!"

if __name__ == "__main__":
    # If this script is run directly, print the hello world message
    print(hello_world())
