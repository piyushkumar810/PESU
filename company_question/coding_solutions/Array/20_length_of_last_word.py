# =====================================================
# LeetCode 58: Length of Last Word
# =====================================================
#
# QUESTION:
# Given a string containing words and spaces,
# return the length of the last word.
#
# A word contains only non-space characters.
#
# Example 1:
# Input:  "Hello World"
# Output: 5
# Explanation: The last word is "World".
#
# Example 2:
# Input:  "   fly me   to   the moon   "
# Output: 4
# Explanation: The last word is "moon".
#
# APPROACH:
# 1. Start from the end of the string.
# 2. Skip all trailing spaces.
# 3. Count characters until we reach another space.
# 4. Return the count.
# =====================================================


class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        # Start at the last character
        i = len(s) - 1

        # Store the length of the last word
        length = 0

        # Step 1: Skip spaces at the end
        while i >= 0 and s[i] == ' ':
            i -= 1

        # Step 2: Count the last word
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1

        # Return the length of the last word
        return length


# =====================================================
# TEST CASES
# =====================================================

solution = Solution()

s1 = "Hello World"
print(solution.lengthOfLastWord(s1))  # Output: 5

s2 = "   fly me   to   the moon   "
print(solution.lengthOfLastWord(s2))  # Output: 4

s3 = "luffy is still joyboy"
print(solution.lengthOfLastWord(s3))  # Output: 6