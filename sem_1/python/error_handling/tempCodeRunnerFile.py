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