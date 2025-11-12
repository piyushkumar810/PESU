# function can return multiple values

def get_values():
    x = 10
    y = 20
    z = 30
    return x, y, z  # returning multiple values
# Calling the function
a, b, c = get_values()

print("a =", a)
print("b =", b)
print("c =", c)


# scope of the function
def outerFunc():
    sample_str = 'Outer Function'
    def innerFunc():
        sample_str = 'Inner Function'
        print(sample_str)
    innerFunc()
    print(sample_str)
outerFunc()


# ----------------------- set compherension
result = {x * y for x in range(4) if x % 2 == 0 for y in range(5) if y > 2}
print(result)


# -------------------------- decorator
def divide(x,y):
    print(x/y)

def outer_div(func):
    def inner(x,y):
        if x < y:
            x,y = y,x
        return func(x,y)
    return inner

divide1 = outer_div(divide)
divide1(2,4)


# Q2)
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

def ordinary():
    print("I am ordinary")

decorated_func = make_pretty(ordinary)
decorated_func()


# Q3)
def uppercase_decorator(function):
    def wrapper():
        func = function()
        return func.upper()
    return wrapper

def split_string(function):
    def wrapper():
        func = function()
        return func.split()
    return wrapper

@split_string
@uppercase_decorator
def say_hi():
    return "hello there"

print(say_hi())


# Q4)
# @a_decorator_passing_arbitrary_arguments
def function_with_arguments(a,b,c):
    print(a,b,c)

function_with_arguments(1,2,3)


# Q6)

if bool("False"):
    print("yes")
else:
    print("No")

'''
Step 1: What does bool("False") mean?

In Python, when you pass something to the bool() function,
it checks if the value is considered “truthy” or “falsy.”

Empty strings → "" → False

Non-empty strings → "anything" → True
'''

if bool(True):
    print("yes")
else:
    print("No")

'''
Because bool() is a type conversion function, it always gives:

True for any non-zero, non-empty, or truthy value.

False for 0, None, False, '', [], {}, etc.
'''

# hashable
def is_hashable(obj):
    try:
        hash(obj)
        return True
    except TypeError:
        return False

print(is_hashable(10))        # True
print(is_hashable((1, 2)))    # True
print(is_hashable([1, 2]))    # False


'''
Python:

Computes a hash for each key ("a", "b").

Stores them in a hash table (an internal structure).

When you look up d["a"], Python re-computes the hash and jumps straight to its slot — making lookups O(1) (very fast).
'''


# difference between premitive and not-premitivee
'''
Primitive Data Types
Definition: Basic, fundamental data types provided by a programming language.

Characteristics:
Simple and not composed of other types.
Directly supported at the language/compiler level.
Store only single values.

Examples in Python:
int → integers (e.g., 5, -10)
float → decimal numbers (e.g., 3.14)
bool → Boolean values (True, False)
str → strings (though in some languages, strings are considered non-primitive)



🌳 Non-Primitive Data Types
Definition: More complex data types built using primitive types.

Characteristics:
Can store multiple values or collections.
Often user-defined or provided as part of libraries.
More flexible and powerful than primitive types.

Examples in Python:
list → ordered collection (e.g., [1, 2, 3])
tuple → immutable ordered collection (e.g., (1, 2, 3))
dict → key-value pairs (e.g., {"name": "Piyush", "age": 21})
set → unique unordered collection (e.g., {1, 2, 3})
User-defined classes → custom objects
'''


# Q argument and parameter
def add(a,b):  #here we use argument
    return a+b
result=add(2,3)  # here we use parameter
print(result)