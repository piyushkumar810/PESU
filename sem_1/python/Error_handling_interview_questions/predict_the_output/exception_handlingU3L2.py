# Q1)

try:
    x = int("abc")
except ValueError:
    print("Invalid")
else:
    print("Valid")
finally:
    print("Done")
'''
output
invalid
done
'''

# Q2)
try:
    print(5 / 1)
except:
    print("Error")
else:
    print("Success")
'''output
5.0
success
'''

# Q3). What will be the output?
try:
    print("A")
except:
    print("B")
else:
    print("C")
finally:
    print("D")

'''
A. A C D
B. A D
C. A B D
D. A C

✅ Answer: A

Explanation:
No exception → try runs
else runs
finally ALWAYS runs
'''


# Q4. What will be the output?
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Error")
else:
    print("No Error")
finally:
    print("Done")

'''
A. Error
B. Error Done
C. No Error Done
D. Program crashes

✅ Answer: B

Explanation:
Exception → except runs → else skipped → finally runs.
'''


# Q5). Which of the following is INVALID?

'''
# A.
try:
    x = 10
finally:
    print("Done")

# B.
try:
    x = 10
except:
    print("Error")

# C.
try:
    x = 10
else:
    print("Ok")


# D.
try:
    x = 10
except:
    print("Error")
finally:
    print("Done")
'''
'''
# ✅ Answer: C

Explanation:
❌ try + else is NOT allowed without except.
'''


# Q6). What happens if finally contains a return statement?
def test():
    try:
        return 1
    finally:
        return 2

print(test())

'''
A. 1
B. 2
C. Error
D. None

✅ Answer: B

Explanation:
finally overrides return from try.
'''


# Q7). What will be printed?
try:
    int("abc")
except ValueError:
    print("Value")
except:
    print("General")

'''
A. Value
B. General
C. Error
D. Nothing

✅ Answer: A

Explanation:
Specific except is checked before general.
'''


# Q8). What will be the output?
try:
    x = 5 / 1
except:
    print("Error")
else:
    print("Success")

'''
A. Error
B. Success
C. Nothing
D. Program crashes

✅ Answer: B

Explanation:
No exception → else executes.
'''


# Q9). Which block is BEST for closing files or releasing resources?
'''
A. try
B. except
C. else
D. finally

✅ Answer: D

Explanation:
finally executes whether exception occurs or not.
'''


# Q10). What happens here?
try:
    print(1 / 0)
except ValueError:
    print("Value Error")

'''
A. Value Error
B. ZeroDivisionError printed
C. Program crashes
D. Nothing

✅ Answer: C

Explanation:
No matching except → program terminates.
'''


# Q11). Which statement is TRUE?
'''
A. finally executes only if exception occurs
B. else executes even when exception occurs
C. except is compulsory
D. else executes only when no exception occurs

✅ Answer: D
'''


# Q12. Identify the output
try:
    print("Try")
    raise ValueError
except:
    print("Except")
else:
    print("Else")
finally:
    print("Finally")

'''
A. Try Else Finally
B. Try Except Finally
C. Except Finally
D. Try Finally

✅ Answer: B

Explanation:

raise forces exception
except runs
else skipped
finally runs

⭐ EXAM MEMORY TIP

else → success
except → failure
finally → ALWAYS

No matching except → CRASH
'''