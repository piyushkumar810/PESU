# Q1)Predict output
class E(Exception): pass

try:
    print("A")
    raise E
except E:
    print("B")
finally:
    raise

'''output
A
B
Traceback (E)
'''

# Q2) Why is raise inside finally dangerous?
'''
✅ Answer:
Because it forces program crash, even if error was handled.
'''

# Q3)dentify the error
class Error:
    pass
raise Error

'''
✅ Answer:
❌ Not an exception → must inherit from Exception
'''

# Q4). What is the output?
class MyError(Exception):
    pass

try:
    print("A")
    raise MyError
except MyError:
    print("B")
    raise
finally:
    print("C")

'''
A. A B C
B. A B C MyError
C. A C
D. Program crashes without output

✅ Answer: B
Explanation:

A printed
MyError raised → handled → B
raise re-throws error
finally ALWAYS executes → C
Program crashes after that
'''


# Q5). What will be printed?
def f():
    try:
        return "Try"
    finally:
        print("Finally")

print(f())

'''
A. Try
B. Finally
C. Finally Try
D. None

✅ Answer: C

Explanation:
finally executes before return is completed
'''


# Q6). Output?
try:
    print("Start")
    raise IndexError
except ValueError:
    print("Value")
else:
    print("Else")
finally:
    print("End")

'''
A. Start Value End
B. Start Else End
C. Start End IndexError
D. Start End

✅ Answer: C
Explanation:

No matching except
finally executes
Program crashes
'''


# 🔴 SECTION B: Ultra-Advanced Code Reasoning
# Q7). Why does this code CRASH?
class E(Exception):
    pass

try:
    raise E
except E:
    print("Handled")
finally:
    raise

'''
✅ Answer:
Because raise inside finally re-throws the exception, forcing program termination even after handling.
'''


# Q8). Predict output
try:
    print("A")
    try:
        raise ValueError
    finally:
        print("B")
except ValueError:
    print("C")
finally:
    print("D")

'''
✅ Answer:

A
B
C
D


Explanation:
Nested finally → outer except → outer finally
'''


# Q9). Identify the error
class MyError:
    pass

raise MyError

'''
✅ Answer:
❌ TypeError
Custom exception must inherit from Exception
'''


# Q10). Why is this bad design?
try:
    x = int("abc")
except:
    pass

'''
✅ Answer:

Error silently ignored

Debugging becomes difficult

Real issues hidden
'''


# Q11). Predict output
try:
    print("Try")
    raise Exception
except:
    print("Except")
else:
    print("Else")
finally:
    print("Finally")
    raise

'''
✅ Answer:

Try
Except
Finally
Exception
'''


# 🔴 SECTION C: Ultra-Advanced Concept Questions (EXAM GOLD ⭐)
# Q12). Why is raise preferred over returning error codes?
'''
✅ Forces error handling
✅ Cleaner logic
✅ Prevents silent failures
'''


# 13. Why must custom exceptions inherit from Exception?
'''
✅ Python only recognizes subclasses of Exception as valid exceptions
'''


# 14. Why is raise inside finally considered dangerous?
'''
✅ It overrides all previous handling
✅ Forces crash
✅ Prevents graceful recovery
'''


# 15. When should else be used instead of code in try?
'''
✅ For success-only logic
✅ To avoid catching unintended exceptions
'''

# 16. Can try exist without except?
'''✅ YES → if finally exists'''