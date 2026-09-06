'''
The Product of Array Except Self, problem is a common interview question.

Problem:-
Given an integer array nums, return an array answer such that:

answer[i] = product of all elements in nums except nums[i]
Do not use division
Must run in O(n) time.

Example:

Input:  nums = [2,4,6,8]
Output: [192,96,64,48]


working:- 
2 → 4 × 6 × 8 = 192
4 → 2 × 6 × 8 = 96
6 → 2 × 4 × 8 = 64
8 → 2 × 4 × 6 = 48
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