# What is a Lambda Function?
'''
A lambda function is a small, unnamed (anonymous) function in Python — 
used for short, simple operations.
'''

# Normal function:
def add(a, b):
    return a + b

# Same with lambda:
add = lambda a, b: a + b
print(add(3, 5))   # Output: 8


# syntax: - lambda arguments:expression
'''
-- No def keyword
-- No function name
-- Just one line expression
'''

# Q) wap create a lambda function taking two argument a and b find a^b
square=lambda a,b : a**b
print(square(3,4))

# --------------- lambda function basically used with built-in functions (map, filter, reduces)

# use with map()
# map()--> apply a function to each element  (syntax:- map(function, iterable))
number=[2,4,6,8,9]
sqr= list(map(lambda x:x**2, number))
print(sqr)


# use with filter()
# filter()->filter items using a condition (syntx-> filter(function, iterable))
num=[1,2,23,5,56,8,4,56,3,4,66767,86]
flt=list(filter(lambda x:x%2==0, num))
print(flt)

# use with reduce()
# reduce()-> apply a rolling computation (needs functools)
from functools import reduce
lst=[1,2,4,6,7]
product=reduce(lambda x,y:x*y , lst)
print(product)

# ------------------------------------------- real example--------------------------------
students = [("raj", 75), ("piyush", 90), ("ramesh", 60)]
# sort by marks
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)
