
"""
LeetCode 67: Add Binary

Given two binary strings a and b, return their sum
as a binary string.

Example:
Input: a = "11", b = "1"
Output: "100"

Approach:
1. XOR calculates the sum without carry.
2. AND followed by left shift calculates the carry.
3. Repeat until there is no carry.

Time Complexity: O(max(m, n))
Space Complexity: O(max(m, n)) for the resulting binary string.
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:

        x = int(a, 2)
        y = int(b, 2)

        while y:
            answer = x ^ y
            carry = (x & y) << 1

            x = answer
            y = carry

        return bin(x)[2:]


# Example
a = "11"
b = "1"

solution = Solution()
print(solution.addBinary(a, b))

# Output: 100
