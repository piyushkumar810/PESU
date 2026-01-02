# 12. Build a text-based calculator. Accept operations from the user. 
#    Raise a custom OperationError for unsupported operations. 
# Raise a custom InputError when inputs are invalid. Keep the program running until the user exits.

# Custom Exceptions
class OperationError(Exception):
    pass

class InputError(Exception):
    pass


def calculator():
    print("Simple Calculator")
    print("Operations: +  -  *  /")
    print("Type 'exit' to quit\n")

    while True:
        try:
            op = input("Enter operation (+, -, *, /) or exit: ")

            if op.lower() == "exit":
                print("Calculator exited.")
                break

            if op not in ['+', '-', '*', '/']:
                raise OperationError("Unsupported operation")

            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
            except ValueError:
                raise InputError("Invalid numeric input")

            if op == '+':
                result = a + b
            elif op == '-':
                result = a - b
            elif op == '*':
                result = a * b
            elif op == '/':
                if b == 0:
                    raise InputError("Division by zero not allowed")
                result = a / b

            print("Result:", result, "\n")

        except OperationError as oe:
            print("Operation Error:", oe, "\n")

        except InputError as ie:
            print("Input Error:", ie, "\n")


# Run calculator
calculator()
