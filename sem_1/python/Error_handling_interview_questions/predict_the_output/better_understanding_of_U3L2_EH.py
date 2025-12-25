# 🧠--------------------- EXCEPTION HANDLING - FULL CLARITY GUIDE (NO CONFUSION)

# 🔹 First, the BASIC STRUCTURE
'''
try:
    # risky code (may cause error)
except:
    # runs ONLY if error occurs
else:
    # runs ONLY if NO error occurs
finally:
    # runs ALWAYS
'''

'''
➡️ Important:

except → error case

else → success case

finally → cleanup case
'''



# 🔷 QUESTION 4
# Which block executes ONLY when NO exception occurs?
# ✅ Answer: else
'''
🔍 WHY?

Because:
try → attempt
except → failure
else → success

🔹 Real-Life Example
“If exam goes well, celebrate”

🧪 Code Example 1 (NO exception → else runs)
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Error occurred")
else:
    print("Success! No error")

✅ Output
Success! No error


🧪 Code Example 2 (exception occurs → else skipped)
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error occurred")
else:
    print("Success! No error")

✅ Output
Error occurred

➡️ else did NOT run.
'''


# 🔷 QUESTION 8
# Which statement is TRUE?
# ✅ Correct: Multiple except blocks are allowed
'''
🔍 WHY?

Different errors need different handling.

🧪 Example (Multiple except blocks)
try:
    x = int("abc")
except ValueError:
    print("Wrong value")
except ZeroDivisionError:
    print("Division error")

✅ Output
Wrong value
'''
'''
➡️ Python checks top to bottom and executes the matching except.
❌ Why other options are wrong?

A. try block cannot exist without except ❌

try:
    print("Hello")
finally:
    print("Done")

✔ VALID code → except is NOT compulsory



B. finally block is mandatory ❌

✔ finally is OPTIONAL


D. else block runs even if exception occurs ❌

❌ else runs ONLY when no exception occurs
'''


# 🔷 QUESTION 10
# What happens if NO except block matches the error?
# ✅ Answer: Program crashes
'''
🧪 Example
try:
    print(10 / 0)
except ValueError:
    print("Value error")

❌ Output
ZeroDivisionError: division by zero


➡️ No matching except, so program terminates.

🧠 Rule:

If Python cannot find a matching except, it crashes the program
'''


# 🔷 QUESTION 14
# Run success code ONLY when no exception occurs
# ✅ Use: else
'''
🧪 Best Practical Example
try:
    x = int(input("Enter number: "))
except ValueError:
    print("Invalid input")
else:
    print("You entered:", x)


➡️ Success message only prints when input is valid.

🔥 NOW LET’S CLEAR ALL YOUR DOUBTS (IMPORTANT RULES)
❓ Is except compulsory?
❌ NO

Valid:

try:
    print("Hello")
finally:
    print("Always runs")

❓ Is finally compulsory?
❌ NO

Valid:

try:
    x = 10 / 2
except ZeroDivisionError:
    print("Error")

❓ Is else compulsory?
❌ NO

Used ONLY when you want:

“Run code ONLY if try succeeds”
'''



# ------------------------------ vvi-----------------------------

# ❓ Which combinations are VALID?
'''
✅ VALID
try + except
try + finally
try + except + finally
try + except + else
try + except + else + finally
'''

'''
❌ INVALID
try alone ❌
try + else ❌
try + else + finally ❌
'''

'''
🧠 ONE-LINE MEMORY TRICK (EXAM GOLD ⭐)

try → risky work
except → error handling
else → success work
finally → cleanup (always)
'''


# 🔚 FINAL REAL-WORLD SCENARIO
# File handling example
try:
    file = open("data.txt")
except FileNotFoundError:
    print("File missing")
else:
    print("File read successfully")
finally:
    file.close()
    print("File closed")


# ➡️ Perfect use of all blocks