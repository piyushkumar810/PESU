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
num2=["piyush","paarneet","rohit","priyanshu"]
uped=[i.upper() for i in num2]
print(uped)

# ✅ Example 4: Add 5 to every number greater than 10
num3=[3,6,10,13,54,6,8,9]
increment=[i+5 for i in num3 if(i>10)]
print(increment)

# 🧠 4️⃣ Advanced / Nested Comprehensions
# 🔹 Example 1: Flatten a 2D list
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
print(flat)  # [1, 2, 3, 4, 5, 6]


# example 2:- pair every number with every letter
num=[1,2,3]
letter=["a","b","c"]
pair=[(n,l) for n in num for l in letter]
print(pair)