
"""
LeetCode 190: Reverse Bits

Question:
Reverse the bits of a given 32-bit unsigned integer.

Example:
Input:  n = 43261596
Output: 964176192

Approach:
1. Extract the last bit of n using AND (& 1).
2. Shift the result left by one position.
3. Add the extracted bit to the result.
4. Shift n right by one position.
5. Repeat exactly 32 times.

Time Complexity: O(1), because we always process 32 bits.
Space Complexity: O(1).
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        for i in range(32):

            # Extract the last bit of n
            bit = n & 1

            # Make space for the next bit
            result = result << 1

            # Add the extracted bit
            result = result | bit

            # Remove the last bit from n
            n = n >> 1

        return result


# Example
n = 43261596

solution = Solution()
print(solution.reverseBits(n))

# Output: 964176192
