if 0:
    print("x")
else:
    print("y")


'''
✅ What is happening?
In Python:

0 is considered False
Any non-zero number is True
So:
if 0: → means → if False:
Therefore the if block does NOT run, and the else block executes.

⭐ Output
y
'''

# 🧠 Why is 0 False?

# In Python, these values are treated as False:
'''
0
0.0
None
False
"" (empty string)
[] (empty list)
{} (empty dict)
set()
()

Everything else is True.
'''