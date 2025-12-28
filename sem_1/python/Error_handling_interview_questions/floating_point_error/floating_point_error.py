# A floating-point error happens because computers store decimal numbers in binary, and many decimal fractions cannot be represented exactly in binary.
# So Python stores a very close approximation, not the exact value.

# 🔴 Classic Example
print(0.1 + 0.2)

'''
❌ Output
0.30000000000000004

❓ Why this happens
0.1 and 0.2 cannot be stored exactly in binary
Their approximations add up to a tiny extra value

👉 This is not a Python bug — it's how floating-point math works on computers.
'''

# 🔴 Comparison Error Example
if 0.1 + 0.2 == 0.3:
    print("Equal")
else:
    print("Not Equal")
'''
❌ Output
Not Equal

Even though mathematically it should be equal, the binary approximation causes failure.
🔴 Accumulation Error (Loop)
'''

total = 0.0
for i in range(10):
    total += 0.1

print(total)
'''
❌ Output
0.9999999999999999
'''

# -----------------------------✅ How to Handle Floating-Point Errors
# ✅ 1. Use round()
print(round(0.1 + 0.2, 2))
'''
# ✔ Output:
# 0.3
'''


# ✅ 2. Compare with a Tolerance (Best Practice)
a = 0.1 + 0.2
b = 0.3

if abs(a - b) < 1e-9:
    print("Equal")

'''
✔ Output:
Equal
'''


# ✅ 3. Use decimal module (High Precision)
from decimal import Decimal

a = Decimal("0.1")
b = Decimal("0.2")

print(a + b)

'''
✔ Output:
0.3


📌 Use this for:
Financial calculations
Scientific accuracy
Banking systems
'''

'''
🧠 Important Notes
Concept                                     	Explanation
Binary representation	                   Some decimals can't be stored exactly
Tiny errors	Usually around                           1e-16
Avoid  ==	                                  Use tolerance instead
Decimal	                                           Exact but slower
'''


# 📌 Interview One-Liner
# Floating-point errors occur because decimal numbers are stored as binary approximations, leading to small precision inaccuracies.