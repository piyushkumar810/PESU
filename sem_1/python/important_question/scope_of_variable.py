# 1️⃣ What is Scope?
# Scope defines where in the program a variable can be accessed or modified.
# Think of it like a “visibility area” for a variable.

# 🧠 Example:
x = 10  # Global scope

def show():
    y = 20  # Local scope
    print(x)  # Accessible (global)
    print(y)  # Accessible (local)

show()
print(x)  # Accessible
# print(y)  # ❌ Error - y is local to show()

# 🔍 Output:
# 10
# 20
# 10
# NameError: name 'y' is not defined

# 💡 Summary:
# Local scope — variables inside a function.
# Global scope — variables outside all functions (top-level).


# 🔄 2️⃣ What is Lifetime?
# Lifetime defines how long a variable exists in memory.

# 🧠 Example:
def func():
    x = 100  # created when func() starts
    print("Inside function:", x)

func()
print("Outside function:", x)  # ❌ x no longer exists


# Explanation:
# x exists only during the function execution.
# After the function finishes, its memory is released — so the lifetime ends.

# ✅ Scope → where
# ✅ Lifetime → how long


# ⚙️ 3️⃣ The LEGB Rule (Python’s Variable Lookup Order)
# When Python sees a variable name, it looks for it in this order:

# Order	Scope Type	Example	Description
# L	Local	Inside current function	Variables defined inside a function
# E	Enclosing	Outer function (if nested)	Variables in parent functions
# G	Global	Top-level of script	Variables declared globally
# B	Built-in	From Python itself	len, print, max, etc.
# 🧠 Example — LEGB in action:
x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print("Inside inner:", x)
    inner()
    print("Inside outer:", x)

outer()
print("Outside all:", x)


# Output:

# Inside inner: local
# Inside outer: enclosing
# Outside all: global


# Explanation:
# Python looks for x in this order:
# 👉 Local → Enclosing → Global → Built-in


# 🏗️ 4️⃣ Enclosing Scope (Nested Functions)
# When one function is defined inside another, the inner function can access variables from its outer one.

def outer():
    message = "Hello"
    def inner():
        print(message)  # Can access outer variable
    inner()

outer()


# ✅ Works fine — inner() has access to message due to enclosing scope.


# 🧱 5️⃣ Global Keyword
# If you want to modify a global variable inside a function, you must use the global keyword.

x = 10

def change():
    global x
    x = 20  # modifies global x

change()
print(x)  # Output: 20


# Without global, Python creates a new local x, leaving the global one unchanged.


# 🪄 6️⃣ Nonlocal Keyword
# Used when you have nested functions and want the inner one to modify the outer one’s variable.

def outer():
    x = 5
    def inner():
        nonlocal x
        x = 10
    inner()
    print(x)

outer()  # Output: 10


# Here, nonlocal x tells Python to refer to the x in the enclosing function, not the global or local one.


# 🎁 7️⃣ Packing & Unpacking

# --------------✅ Packing
# Collects multiple values into one variable (tuple by default):

def pack_values(*args):
    print(args)

pack_values(1, 2, 3)
# Output: (1, 2, 3)

# ----------------✅ Unpacking
# Extracts elements of a tuple/list into individual variables:

data = (10, 20, 30)
a, b, c = data
print(a, b, c)
# Output: 10 20 30

# ⚖️ 8️⃣ Scope vs Lifetime — Comparison
# Feature	Scope	Lifetime
# Meaning	Where a variable is accessible	How long it exists in memory
# Type	Spatial (location-based)	Temporal (time-based)
# Example	Local, Global, etc.	Until function ends or program exits
# 🧩 9️⃣ Quick Concept Recap
# Concept	Keyword / Example	Key Idea
# Local	Variable inside function	Exists during function call
# Enclosing	Outer function variable	Accessible by inner function
# Global	Declared outside all functions	Accessible anywhere
# Built-in	e.g., len, print	Always available
# global	Modify global variable	Inside function
# nonlocal	Modify outer variable	Inside nested functions
# Packing	*args	Collect many values
# Unpacking	a,b = (1,2)	Distribute tuple element

# -------------------------------------- important ----------------------------------------
from datetime import datetime

now = datetime.now()
print(now.isoformat())


'''
⏰ ISO Format for Date + Time
If you include time, the full ISO datetime format looks like this:
YYYY-MM-DDTHH:MM:SS

2025-11-12T16:45:30.123456
'''


z=10

def change():
    print("inside the function: ",z)
    global z
    z=20
    print("inside the function after changing value: ",z)

change()
print("outside  the function: ",z)



x = 10

def change():
    global x   # tells Python: “use the global x”
    x = 5
    print("Inside function:", x)

change()
print("Outside function:", x)
