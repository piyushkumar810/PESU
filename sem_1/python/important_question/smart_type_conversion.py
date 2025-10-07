'''
read one input as string, 
if it represent an integer (eg."42"), print int <value>
else is it represents a float(eg."3.14"), print float <value> with two decimal place
otherwise print string <value>
'''


# ----------------------- my assumption ---------------------------

# def type_conversion(value):
#     type_of=type(value)
#     print(type_of)
#     if(type_of == float):
#         print(f"it is of float type = {float(value):.2f}")
#     elif(type_of == int):
#         print(f"it is of integer type = {int(value)}")
#     else:
#         print(f"it is string only = {value}")

# str=42.12
# type_conversion(str)


# --------------------------- actually we have to do this --------------------------
str=input("Enter a Value : ").strip()
try:
    num=int(str)
    print("int", num)
except ValueError:
    try:
        # try to convert to float 
        f=float(str)
        if f.is_integer():
            print("int", int(f))
        else:
            print("float","{:.2f}".format(f))
    except ValueError:
        print("string ", str)

# note
# what does is_integer() do
'''
f.is_integer()
Checks if the number has no decimal part.

Example:
5.0 → is_integer() = True
3.14 → is_integer() = False
'''

# what try and except block used
'''
“Try to do something. If it fails, don't crash, just do something else.”
'''

# What is ValueError?
'''
It's an error type that happens when you try to convert something to a number, 
but it's not possible.
eg:-
int("abc")  # ❌ gives ValueError
'''