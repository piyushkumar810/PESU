'''
Two Sum
Problem Statement

Given an array of integers nums and an integer target, return the indices of the two numbers such 
that they add up to the target.

You may assume that:

Exactly one solution exists.
You cannot use the same element twice.

example:
nums = [2,7,11,15]
target = 9

output=[0,1]
'''
def two_sum(num, target):
    l_n = len(num)

    for i in range(l_n):
        for j in range(i + 1, l_n):
            if num[i] + num[j] == target:
                return [i, j]

    return -1

num = [10,20,4,20,3,4,6,3454,64]
target = int(input("Enter the value: "))

print(two_sum(num, target))
# got 3/5 bad time complexity


# ------------------------ 5/5 better time complexity 
def two_sum(nums, target):
    seen = {}
    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in seen:
            return [seen[complement], i]

        seen[nums[i]] = i

    return -1


nums = [10, 20, 4, 20, 3, 4, 6, 3454, 64]
target = int(input("Enter the target value: "))
print(two_sum(nums, target))