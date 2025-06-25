"""
Hello World module.

This module provides a simple function to print "Hello, World!".
"""

def hello_world():
    """
    Print "Hello, World!" to the console.
    
    Returns:
        str: The string "Hello, World!"
    """
    message = "Hello, World!"
    print(message)
    return message

if __name__ == "__main__":
    # Execute the function when the script is run directly
    hello_world()