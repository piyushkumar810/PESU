# -------------------------------------- decorators --------------------------------------
# extra functionality to your function

# In Python, a decorator is a special function that is used to modify or enhance the behavior of another function or class — without permanently changing its code.

# it also support multiple optional behaviour
# you can also use @ symbol to use decorator
# decortors are mostly used with flask and zanjo


# # creating outer function
# def make_pretty(func):
#     # defining the inner function
#     def inner():
#         print("i got decorator")

#         # calling original function
#         func()
#     # returning inner function   
#     return inner

# eg:-- 
def divide(x,y):
    print(x/y)

def outer_func(func):
    def inner(x,y):
        if(x<y):
            x,y=y,x
            return func(x,y)
    return inner

divide1=outer_func(divide)
divide1(2,4)


# multiple decorator can be applied to single function

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


