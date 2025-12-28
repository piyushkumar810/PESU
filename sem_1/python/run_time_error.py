'''
except Exception as e
what does it will print ZeroDivisionError or inside it the message

Very good question 👍
This is a core concept in exception handling. Let's clear it 100% clearly.

Short Answer (exam-ready)
except Exception as e:
    print(e)


👉 It prints the ERROR MESSAGE, not the error type name.

Let's see with an example 🔍
Code
try:
    a = 10
    b = 0
    res = a / b
except Exception as e:
    print(e)

Output
division by zero


❌ It does NOT print:

ZeroDivisionError

Why does this happen?

Exception → base class of all runtime errors

e → object containing details of the error

print(e) → prints the error message stored inside the exception

For ZeroDivisionError, the message is:

division by zero

If you want to print the ERROR TYPE 🔥
Method 1: Using type(e)
except Exception as e:
    print(type(e))


Output:

<class 'ZeroDivisionError'>

Method 2: Print BOTH error type and message (BEST PRACTICE)
except Exception as e:
    print(type(e).__name__, ":", e)


Output:

ZeroDivisionError : division by zero
'''



# --------------------use os assert
'''
✅ Short Answer

YES, if an assert fails inside a try block, the except block WILL execute
because assert raises an AssertionError.

🔍 Why does this happen?
assert is NOT like if

if → logical check (no error)

assert → error check (raises exception if condition is false)

Syntax
assert condition, "optional message"


If condition is False →

AssertionError

🧪 Example 1: assert INSIDE try (except executes)
try:
    a = 12
    assert a / 2 == 0, "Condition failed"
    print("LOra")
except Exception as e:
    print("Except executed:", e)
else:
    print("Else executed")
finally:
    print("Finally executed")

Output
Except executed: Condition failed
Finally executed


✔️ assert fails
✔️ Raises AssertionError
✔️ except executes

🧪 Example 2: assert PASSES (except NOT executed)
try:
    a = 0
    assert a / 2 == 0
    print("LOra")
except Exception as e:
    print("Except:", e)
else:
    print("Else executed")
finally:
    print("Finally executed")

Output
LOra
Else executed
Finally executed

🧠 Key Difference (VERY IMPORTANT)
Statement	Raises Exception?	except runs?
if condition_false	❌ No	❌ No
assert condition_false	✅ Yes (AssertionError)	✅ Yes
'''