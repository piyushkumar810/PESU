# Use reduce() to find the maximum number in a list without using max().

from functools import reduce

# Given list
numbers = [3, 7, 2, 9, 5, 10, 6]

# Use reduce() to find maximum
max_num = reduce(lambda a, b: a if a > b else b, numbers)

print("Maximum number:", max_num)
