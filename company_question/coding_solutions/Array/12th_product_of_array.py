'''
The Product of Array Except Self problem is a common interview question.

Problem

Given an integer array nums, return an array answer such that:

answer[i] = product of all elements in nums except nums[i]
Do not use division
Must run in O(n) time.

Example:

Input:  nums = [1,2,3,4]
Output: [24,12,8,6]
'''

def productExceptSelf(nums):
    n = len(nums)
    answer = [1] * n

    # Prefix products
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    # Suffix products
    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer

nums=[2,4,6,8]
print(productExceptSelf(nums))