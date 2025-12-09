# Part C – Hard / Coding Questions
# Write a program that:

'''
Q1)Reads two numbers
Divides them
Uses try, except, else, finally
'''
def two_number(n,m):
    try:
        z=n+m
        print("sum is ", z)

    except Exception as e:
        print("error is : ", e)

    else:
        print("it cannot be bivided by 0")

    finally:
        print("this code block will run in any ciondition")

n=int(input("enter the value : "))
m=int(input("enter the value : "))
two_number(n,m)
    

'''
Q2)Write a program to catch multiple exceptions:

ValueError  
ZeroDivisionError  
TypeError
'''


# Q3)Create a custom exception “InvalidMarkError” and raise it if marks > 100 or < 0.

# Q4)Write a program that handles file opening errors using try…except…finally.

# Q5)write code that raises an exception when temperature < −50 or > 60.