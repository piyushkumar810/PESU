
# Q1)

def fun():
    print(x)
    x = 10
fun()
# ------------or
x=10
def fun():
    print(x)
    x = 10
fun()
'''both will give:- UnboundLocalError: cannot access local variable 'x' where it is not associated with a value '''


# Q2)
try:
    print(10 / 0)
except ValueError:
    print("Value Error")
'''✅ Answer: Program crashes with ZeroDivisionError
Explanation: ZeroDivisionError is not handled.'''


# Q3)
# x = 999999999999999999999 ** 999
'''✅ Answer:
✔ No error
✔ Python supports large integers (no overflow)'''