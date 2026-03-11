def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def calculator():
    print("Simple Calculator")
    print("Available operations: +, -, *, /")
    print("Type 'quit' to exit")
    
    while True:
        try:
            user_input = input("\nEnter calculation (e.g., 5 + 3) or 'quit': ")
            
            if user_input.lower() == 'quit':
                print("Goodbye!")
                break
            
            # Parse the input
            parts = user_input.split()
            if len(parts) != 3:
                print("Please enter in format: number operator number")
                continue
            
            num1 = float(parts[0])
            operator = parts[1]
            num2 = float(parts[2])
            
            # Perform calculation
            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
            else:
                print("Invalid operator. Use +, -, *, or /")
                continue
            
            print(f"Result: {num1} {operator} {num2} = {result}")
            
        except ValueError:
            print("Please enter valid numbers")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")

def main():
    calculator()

if __name__ == "__main__":
    main()
