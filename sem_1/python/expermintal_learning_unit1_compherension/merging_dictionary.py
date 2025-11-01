# Merge two dictionaries and keep the maximum value for each common key using comprehension.

# Example dictionaries
dict1 = {'raj': 30000, 'piyush': 37000, 'rohit': 53000}
dict2 = {'piyush': 40000, 'rohit': 52000, 'priyanshu': 75000}

# Merge and keep the maximum value for common keys
merged_dict = {
    key: max(dict1.get(key, 0), dict2.get(key, 0))
    for key in set(dict1) | set(dict2)
}

print(merged_dict)
