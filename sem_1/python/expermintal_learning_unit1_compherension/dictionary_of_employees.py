# From a dictionary of employees and salaries, create a dictionary of only those earning more than ₹50,000.

dictionary_of_employee = {
    "raj": 30000,
    "ramesh": 55000,
    "piyush": 37000,
    "praneeth": 65000,
    "rohit": 53000,
    "priyanshu": 75000
}

# Extract employees with salary greater than 50000
extract_employees = {name: salary for name, salary in dictionary_of_employee.items() if salary > 50000}

print(extract_employees)


# Explanation:
# .items() gives both employee name and salary.

# ----------------------- if you want to fetch index wise element

# convert dict_items to list first
items_list = list(dictionary_of_employee.items())

print(items_list[0])   # 0th element (first key-value pair)
