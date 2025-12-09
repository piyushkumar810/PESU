# Part C – Hard / Coding Questions
# Write a program that:

'''
Q1)Reads two numbers
Divides them
Uses try, except, else, finally
'''
try:
    # reading two numbers
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    # division (may cause ZeroDivisionError)
    result = a / b

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

except ValueError:
    print("Error: Please enter only numbers!")

else:
    # runs only when NO error occurs
    print("Division successful!")
    print("Result =", result)

finally:
    # always runs
    print("Program Ended.")

    

'''
Q2)Write a program to catch multiple exceptions:

ValueError  
ZeroDivisionError  
TypeError
'''

def handling_error():
    try:
        a = input("Enter first number: ")
        b = input("Enter second number: ")
    
        # Convert to integers (may raise ValueError)
        a = int(a)
        b = int(b)
    
        # Division (may raise ZeroDivisionError)
        result = a / b
    
        # TypeError example (doing invalid operation) 
        x = result + "hello"   # This will raise TypeError
    
    except ValueError:
        print("Error: You entered an invalid number! (ValueError)")
    
    except ZeroDivisionError:
        print("Error: Cannot divide a number by zero! (ZeroDivisionError)")
    
    except TypeError:
        print("Error: Invalid operation between different data types! (TypeError)")
    
    else:
        print("Operation successful!")
        print("Result:", result)
    
    finally:
        print("Program Finished.")

handling_error()


# Q3)Create a custom exception “InvalidMarkError” and raise it if marks > 100 or < 0.


# Q4)Write a program that handles file opening errors using try…except…finally.

# Q5)write code that raises an exception when temperature < −50 or > 60.