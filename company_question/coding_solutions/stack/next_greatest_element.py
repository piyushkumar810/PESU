'''3. Next Greater Element ⭐⭐⭐⭐⭐🔥

This is one of the most important monotonic stack problems.

Problem:-
For every element, find the next greater element to its right.

Example:

Input:
[4, 5, 2, 10, 8]

Output:

[5, 10, 10, -1, -1]

Why?

4 → 5
5 → 10
2 → 10
10 → -1
8 → -1
'''

# Brute Force Idea
# For every element, search to the right.

def next_greater(nums):

    result = []

    for i in range(len(nums)):

        greater = -1

        for j in range(i + 1, len(nums)):

            if nums[j] > nums[i]:
                greater = nums[j]
                break

        result.append(greater)

    return result
'''
This works, but complexity is:

O(n²)
'''
'''
We can do better.
Optimized Solution — Monotonic Stack ⭐⭐⭐⭐⭐
'''

def next_greater(nums):

    result = [-1] * len(nums)

    stack = []

    for i in range(len(nums) - 1, -1, -1):

        # Remove smaller elements
        while stack and stack[-1] <= nums[i]:
            stack.pop()

        # Top is the next greater element
        if stack:
            result[i] = stack[-1]

        # Add current element
        stack.append(nums[i])

    return result


# Test
nums = [4, 5, 2, 10, 8]

print(next_greater(nums))


'''
Output:
[5, 10, 10, -1, -1]
'''