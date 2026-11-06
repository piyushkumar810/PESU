
"""
LeetCode 136: Single Number

Question:
Given a non-empty array of integers, every element appears
twice except for one element.

Find the element that appears only once.

Example 1:
Input: nums = [2, 2, 1]
Output: 1

Example 2:
Input: nums = [4, 1, 2, 1, 2]
Output: 4

Approach:
1. Initialize result = 0.
2. Apply XOR to every element.
3. Duplicate numbers cancel each other because a ^ a = 0.
4. The remaining number is the single number.

Time Complexity: O(n)
Extra Space Complexity: O(1)
"""


def singleNumber(nums):

        result = 0

        for num in nums:
            result = result ^ num

        return result


# Example 1
nums = [2, 2, 1]
print(singleNumber(nums))

# Output: 1


# Example 2
nums = [4, 1, 2, 1, 2]

print(singleNumber(nums))

# Output: 4
