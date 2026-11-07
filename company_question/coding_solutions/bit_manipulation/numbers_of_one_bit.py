
"""
LeetCode 191: Number of 1 Bits

Question:
Given a positive integer n, return the number of set bits
(1s) in its binary representation.

Example:
Input: n = 11
Binary: 1011
Output: 3

Approach:
1. Initialize count = 0.
2. Use n & 1 to extract the last bit.
3. If the extracted bit is 1, increment count.
4. Right shift n by 1 to remove the last bit.
5. Repeat until n becomes 0.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n:
            bit = n & 1

            if bit == 1:
                count += 1

            n = n >> 1

        return count


# Example
n = 11

solution = Solution()
print(solution.hammingWeight(n))