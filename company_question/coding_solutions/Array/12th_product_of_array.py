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
    print(answer)

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


# dry run
'''
def productExceptSelf(nums):

    # nums = [2, 4, 6, 8]

    n = len(nums)

    # n = 4

    answer = [1] * n

    # [1] * 4
    # answer = [1, 1, 1, 1]

    print(answer)

    # Output:
    # [1, 1, 1, 1]


    # -----------------------------------
    # PREFIX PRODUCTS
    # -----------------------------------

    prefix = 1

    # prefix = 1

    for i in range(n):

        # i = 0
        # answer[0] = prefix
        # answer[0] = 1
        # answer = [1, 1, 1, 1]

        answer[i] = prefix

        # prefix *= nums[i]
        # prefix = 1 * nums[0]
        # prefix = 1 * 2
        # prefix = 2

        prefix *= nums[i]


        # i = 1
        # answer[1] = prefix
        # answer[1] = 2
        # answer = [1, 2, 1, 1]

        # prefix = 2 * nums[1]
        # prefix = 2 * 4
        # prefix = 8

        answer[i] = prefix
        # NOTE: In actual execution, this line happens before
        # prefix *= nums[i], so see the corrected sequence below.
'''