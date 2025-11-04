def split_string(function):
    def wrapper():
        func = function()          # Call the original function
        splitted_string = func.split()  # Split the returned string into words
        return splitted_string
    return wrapper


def uppercase_decorator(function):
    def wrapper():
        func = function()          # Call the original function
        make_uppercase = func.upper()  # Convert it to uppercase
        return make_uppercase
    return wrapper


@split_string
@uppercase_decorator
def say_hello():
    return "hello world this is python"


# Calling the decorated function
result = say_hello()
print(result)