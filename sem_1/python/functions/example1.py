# -------------------------- working with a function()---------------------

# creating a function
def greet():
    '''this function returns a greeting message'''
    print("hello everyone ")

greet()


# function with a parameter
# if you accepting one paraameter and you are passing two parameter then you will get an error
print()
def greet_person(name):
    """greeting a persion by his name"""
    print(f"hello {name}")

nam="piyush"
greet_person(nam)


# returning a value
print()
def greet_return(name1):
    '''returning a message"'''
    return f"hello piyush {name1}"

nam1="kumar"
print(greet_return(nam1))

# immutable
print()
def modify(x):
    x=x+10
    print("inside x = ", x)

num2=5
modify(num2)
print('outside x= ', num2)

# mutable
print()
def modify_list(lst):
    lst.append(4)
    print('inside', lst)

number=[1,2,3]
modify_list(number)
print('outside', number)