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
number=[1, 2, 3, 4, 5]
cudes=list(map(lambda a:a**3, number))
print(cudes)


# Q5) Use filter() with lambda to get only odd numbers from the list
#     [10, 15, 20, 25, 30, 35]
lst=[10, 15, 20, 25, 30, 35]
odd_num=list(filter(lambda a:a%2==1, lst))
print(odd_num)


# Q6) Use reduce() with lambda to find the sum of all numbers in [5, 10, 15, 20]
from functools import reduce
num=[5, 10, 15, 20]
sum_of_all=reduce(lambda a,b:a+b , num)
print(sum_of_all)



# 🔹 Level 3: Logical Conditions

# Q7) Write a lambda that checks if a string starts with "A".
    # Example → "Apple" → True, "Banana" → False
user_input=input("enter the fruite name : ").strip()
# check_strring=lambda a:print("True") if(a[0]=='A') else print("False")
# ---------------------------------------------note-----------------------------------
'''
Inside your lambda, you are printing the result (print("Even")) instead of returning it.
The print() function always returns None, so when you do:

it prints “Even” (from inside lambda), and then prints None (from outer print).

✅ Correct Version:
You should make the lambda return a string, not print it:
'''
# ----------------or------------------
check_string = lambda a: a.startswith("A")
print(check_string(user_input))


# Q8) You have this list:
#     names = ["Raj", "Ankit", "Piyush", "Aman", "Ravi"]
#     Use filter() + lambda to get only names that start with "A".
name = ["Raj", "Ankit", "Piyush", "Aman", "Ravi"]
filter_it = list(filter(lambda a: a.startswith("A"), name))
print(filter_it)


# Q9) Write a lambda that returns "Even" if a number is even, otherwise "Odd".
num_int=int(input("enter the number : "))
odd_or_even=lambda a:"Even" if(a%2==0) else "odd"
print(odd_or_even(num_int))



# 🔹 Level 4: Sorting

#Q10)  You have:
# students = [("Raj", 80), ("Piyush", 90), ("Ramesh", 70)]
# Use sorted() with lambda to sort this list by marks in descending order.
student=[("Raj", 80), ("Piyush", 90), ("Ramesh", 70)]
sorted_list=sorted(student,key=lambda x:x[1])
print(sorted_list)