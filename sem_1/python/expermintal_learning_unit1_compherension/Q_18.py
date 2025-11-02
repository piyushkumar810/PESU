# Given two lists — student names and marks — use zip() to display results as tuples.

# Given two lists
students = ["piyush", "rohit", "priyanshu", "praneeth", "tanmay"]
marks = [60, 50, 70, 90, 75]

# Use zip() to pair them as tuples
result = list(zip(students, marks))

print(result)
