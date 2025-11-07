# -------------------------------- list compherension --------------------------------
'''
🧠 What Is List Comprehension?
It's a compact way to create lists from existing iterables (like lists, tuples, or strings).

🧩 2️⃣ Basic Syntax
[expression for item in iterable if condition]
'''

'''
# ------------------------ list of iterables-------------------

🧠 Summary Table

Data Type	                       Iterable?	                       Example of Iteration
List	                           ✅ Yes	                          for x in [1,2,3]: ...
Tuple	                           ✅ Yes	                          for x in (1,2,3): ...
Set	                               ✅ Yes	                          for x in {1,2,3}: ...
String	                           ✅ Yes	                          for x in "abc": ...
Dictionary	                       ✅ Yes	                          for key in dict: ...
Integer / Float	                   ❌ No	                              Not iterable!

'''

# Normal way:
squares = []
for x in range(5):
    squares.append(x * x)
print(squares)   # [0, 1, 4, 9, 16]

# Using list comprehension:
squares = [x * x for x in range(5)]
print(squares)   # [0, 1, 4, 9, 16]

# ✅ Example 1: Square of numbers
num=[1,3,5,6,8,9,3]
sq_num=[i**2 for i in num]
print(sq_num)

# ✅ Example 2: Get even numbers only
num1=[1,3,5,6,8,9,3]
even_num=[i for i in num1 if(i%2==0)]
print(even_num)

# ✅ Example 3: Convert all strings to uppercase
'''str="piyush"
uped=str.upper().strip()
print(uped)'''
