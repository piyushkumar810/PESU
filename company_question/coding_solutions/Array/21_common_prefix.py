# =====================================================
# LeetCode 14: Longest Common Prefix
# =====================================================
#
# QUESTION:
# Given a list of strings, find the longest prefix
# shared by every string.
#
# If no common prefix exists, return an empty string.
#
# Example 1:
# Input:  ["flower", "flow", "flight"]
# Output: "fl"
#
# Example 2:
# Input:  ["dog", "racecar", "car"]
# Output: ""
#
# APPROACH:
# 1. Take the first string as the prefix.
# 2. Check whether every other string starts with it.
# 3. If not, remove its last character.
# 4. Repeat until the prefix matches all strings.
# =====================================================

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        # Handle an empty list
        if not strs:
            return ""

        # Initially, take the first string as the prefix
        prefix = strs[0]

        # Check every string in the list
        for word in strs:

            # Keep shortening the prefix until the
            # current word starts with the prefix
            while not word.startswith(prefix):

                # Remove the last character
                prefix = prefix[:-1]

                # If the prefix becomes empty,
                # there is no common prefix
                if not prefix:
                    return ""

        # Return the longest common prefix
        return prefix


# =====================================================
# TEST CASES
# =====================================================

solution = Solution()

strs1 = ["flower", "flow", "flight"]
print(solution.longestCommonPrefix(strs1))  # fl

strs2 = ["dog", "racecar", "car"]
print(solution.longestCommonPrefix(strs2))  # ""

strs3 = ["interspecies", "interstellar", "interstate"]
print(solution.longestCommonPrefix(strs3))  # inters

strs4 = ["apple", "apple", "apple"]
print(solution.longestCommonPrefix(strs4))  # apple
