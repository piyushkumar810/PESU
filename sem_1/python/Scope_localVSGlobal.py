x = 10
def change():
    # print(x)
    x = 20
    print(x)

change()
print(x)  

# --------------------------- predict the output

y=10
def changed():
    print(y)
   
changed()

# q3
def outer():
    x21 = 10
    def inner():
        x21 = 20
    inner()
    print(x21)  #10

outer()
# Explanation: x21 = 20 creates inner local, does not modify enclosing x.



# -------------------------- practice questions --------------------------------
# Try these to test yourself:

# Q1) Create a global variable and modify it using a function with global.



x1=10
def change():
    #print(x1)   #error 
    global x1
    x1=50
    print("inside the function: ", x1)

change()
print("outside the function but changing the global: ", x1)
print()


# Q2) Create a nested function where the inner modifies outer’s variable using nonlocal.



# Q3) Create local, enclosing, and global variables named the same (x) and print all.

def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20
    inner()
    return x

print(outer())


# Q4) Mix global and nonlocal in one program.


# ------------------ mistacks everyone does
x11 = 10
def f():
    global x11
    print(x11)
    x11 = 20
f()

# 4. Assuming nonlocal affects global variables

# x12 = 10
# def outer():
#     def inner():
#         nonlocal x12   # ERROR (no enclosing x)

'''Reason:
nonlocal cannot search the global scope.
It only works between nested functions.'''



# 5. Forgetting that variables defined inside loops/ifs are still local to the function

'''
Wrong assumption:

def f():
    if True:
        x = 10
    print(x)      # candidate thinks error, but works!


Why?
Python does not have block scope.
Loops, if blocks, and try blocks do NOT create new scopes.

'''



# 6. Using mutable global variables incorrectly
'''
Wrong:

lst = []

def f():
    lst = lst + [1]   # ERROR


Why?
Assignment creates local variable → but right side tries to use local variable before assignment → ERROR.

Correct ways:

Option 1: use global
lst = []
def f():
    global lst
    lst = lst + [1]

    
Option 2: modify without assignment (better)
lst = []
def f():
    lst.append(1)

'''



# 7. Assuming inner function sees updated variables without nonlocal
'''
Wrong:

def outer():
    x = 10
    def inner():
        x = 20   # creates local x, does NOT modify outer x
    inner()
    print(x)    # candidate expects 20


Output: 10

Reason:
Assignment creates a new local variable.
To update outer variable → use nonlocal.
'''



# 8. Confusing LEGB rule
'''
Candidates mix up this order:

L – Local  
E – Enclosing  
G – Global  
B – Built-in


Example mistake:

x = 50
def outer():
    x = 20
    def inner():
        print(x)  # expects 50 (global)
    inner()
outer()


Output: 20
(closest matching x is in Enclosing)
'''



# 9. Forgetting closure behavior
'''
Mistake:

def make():
    nums = []
    def add():
        nums = nums + [1]   # ERROR
    return add


Why?
Same reason as mutable globals: assignment makes local variable, shadowing the outer one.

Correct:

def make():
    nums = []
    def add():
        nums.append(1)
    return add
'''


# 10. Using global variables unnecessarily
'''
Interviewers dislike this:

count = 0
def inc():
    global count
    count += 1


Better:

def counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc
'''