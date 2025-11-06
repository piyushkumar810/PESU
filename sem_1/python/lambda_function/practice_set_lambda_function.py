#-------------------------------------- 🧩 Lambda Practice Set
# 🔹 Level 1: Basic

# .Q1)Write a lambda function to find the square of a number.
#          Example → 5 → 25
sqr=lambda a:a*a
print(sqr(5))

# Q2)Write a lambda to find the maximum of two numbers.
#          Example → (10, 15) → 15
max=lambda a,b: a if(a>b) else b
print(f"maximum among two is: {max(7,49)}")

# Q3) Write a lambda that adds 5 to any number passed to it.
#           Example → 7 → 12
passed_number_added=lambda x:x+5
print(f"added 5 to 7 that number : {passed_number_added(7)}")



# 🔹 Level 2: With Built-in Functions

# Q4) Use map() with lambda to convert this list
#    numbers = [1, 2, 3, 4, 5]
#    into a list of their cubes → [1, 8, 27, 64, 125]


# Q5) Use filter() with lambda to get only odd numbers from the list
#     [10, 15, 20, 25, 30, 35]

# Q6) Use reduce() with lambda to find the sum of all numbers in [5, 10, 15, 20]




# 🔹 Level 3: Logical Conditions

# Q7) Write a lambda that checks if a string starts with "A".
    # Example → "Apple" → True, "Banana" → False

# Q8) You have this list:
#     names = ["Raj", "Ankit", "Piyush", "Aman", "Ravi"]
#     Use filter() + lambda to get only names that start with "A".

# Q9) Write a lambda that returns "Even" if a number is even, otherwise "Odd".




# 🔹 Level 4: Sorting

#Q10)  You have:
# students = [("Raj", 80), ("Piyush", 90), ("Ramesh", 70)]
# Use sorted() with lambda to sort this list by marks in descending order.