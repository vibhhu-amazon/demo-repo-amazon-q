"""
Main script to demonstrate the hello_world function.
"""

from hello_world.hello import hello_world


def main():
    """
    Main function that calls and prints the result of hello_world().
    """
    message = hello_world()
    print(message)


if __name__ == "__main__":
    main()