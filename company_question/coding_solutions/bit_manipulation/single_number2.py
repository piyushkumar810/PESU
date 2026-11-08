
"""
LeetCode 137: Single Number II

Question:
Given an integer array nums where every element appears
three times except for one element, which appears exactly once,
find and return the single element.

Example:
Input: nums = [2, 2, 3, 2]
Output: 3

Approach:
1. Check each of the 32 bit positions.
2. Count how many numbers have that bit set.
3. Take count % 3 to remove contributions from repeated numbers.
4. Reconstruct the single number using the remaining bits.

Time Complexity: O(32 * n) = O(n)
Space Complexity: O(1)
"""

class Solution:
    def singleNumber(self, nums):

        result = 0

        # Check all 32 bit positions
        for i in range(32):
            count = 0

            # Count set bits at position i
            for num in nums:
                if (num >> i) & 1:
                    count += 1

            # If remainder is 1, set this bit in result
            if count % 3:
                result |= (1 << i)

        # Convert unsigned 32-bit result to signed integer
        if result >= (1 << 31):
            result -= (1 << 32)

        return result


# Example
nums = [2, 2, 3, 2]

solution = Solution()
print(solution.singleNumber(nums))

# Output: 3