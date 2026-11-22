
"""
LeetCode 5: Longest Palindromic Substring

Question:
Given a string s, return the longest palindromic
substring in s.

Approach:
Expand Around Center
"""

class Solution:

    def longestPalindrome(self, s: str) -> str:

        # Store the longest palindrome found so far
        result = ""

        # Traverse every character in the string
        for i in range(len(s)):

            # --------------------------------
            # CASE 1: ODD LENGTH PALINDROME
            # --------------------------------

            # Consider current character as the center
            left = i
            right = i

            # Expand towards left and right
            while (left >= 0 and right < len(s)
                   and s[left] == s[right]):

                # Calculate current palindrome length
                if right - left + 1 > len(result):

                    # Update the longest palindrome
                    result = s[left:right + 1]

                # Expand in both directions
                left -= 1
                right += 1

            # --------------------------------
            # CASE 2: EVEN LENGTH PALINDROME
            # --------------------------------

            # Consider space between two characters as center
            left = i
            right = i + 1

            # Expand towards left and right
            while (left >= 0 and right < len(s)
                   and s[left] == s[right]):

                # Calculate current palindrome length
                if right - left + 1 > len(result):

                    # Update the longest palindrome
                    result = s[left:right + 1]

                # Expand in both directions
                left -= 1
                right += 1

        # Return the longest palindrome
        return result


# --------------------------------
# MAIN PROGRAM / EXECUTION
# --------------------------------

# Create an object of Solution class
obj = Solution()

# Test Case 1
s = "babad"
print("Input:", s)
print("Longest Palindrome:", obj.longestPalindrome(s))

# Test Case 2
s = "cbbd"
print("Input:", s)
print("Longest Palindrome:", obj.longestPalindrome(s))

# Test Case 3
s = "racecar"
print("Input:", s)
print("Longest Palindrome:", obj.longestPalindrome(s))