# practice of decorator

'''decorator is a function which takes another function as an argunment and return new function that modifies the behaviour of original function
so the new function is often refers as decorators function'''

# ------------------------------
# A SIMPLE DECORATOR EXAMPLE
# ------------------------------

# This is our decorator function
def my_decorator(func):

    # This inner function adds extra behavior
    def wrapper():
        print("Before function runs")   # Extra code (runs before)
        
        func()                          # Call the original function
        
        print("After function runs")    # Extra code (runs after)

    return wrapper   # decorator returns the new modified function


# Using the decorator on a function
@my_decorator
def say_hello():
    print("Hello!")   # Original function


# Calling the decorated function
say_hello()
