x = 10

def change():
   
    print(x)
    x = 20
    print(x)

change()
print(x)  

# ---------------------------
y=10
def changed():
    print(y)
   

changed()

# -------------------------- practice questions --------------------------------
# Try these to test yourself:

# Q1) Create a global variable and modify it using a function with global.
x1=10
def change():
    # print(x1)  error because 
    global x1
    x1=50
    print("inside the function: ", x1)

change()
print("outside the function but changing the global: ", x1)
print()


# Q2) Create a nested function where the inner modifies outer’s variable using nonlocal.



# Q3) Create local, enclosing, and global variables named the same (x) and print all.

# Q4) Mix global and nonlocal in one program.