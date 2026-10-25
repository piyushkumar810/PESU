
"""
Question: LeetCode 205 - Isomorphic Strings

Given two strings s and t, determine whether they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced
to get t, while preserving the order of characters.

Each character must map consistently to one character,
and two different characters cannot map to the same character.

Example 1:
Input: s = "egg", t = "add"
Output: True

Example 2:
Input: s = "foo", t = "bar"
Output: False

Example 3:
Input: s = "paper", t = "title"
Output: True

Approach:
1. Use a dictionary to map characters from s to t.
2. Use another dictionary to map characters from t to s.
3. Check both mappings to ensure they are consistent.
4. Return True if no conflict is found.

Time Complexity: O(n)
Space Complexity: O(k), where k is the number of distinct characters.
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        # Store mappings from s to t
        map_st = {}

        # Store mappings from t to s
        map_ts = {}

        # Check each character at the same position
        for i in range(len(s)):

            # If s[i] already has a mapping,
            # it must match t[i]
            if s[i] in map_st and map_st[s[i]] != t[i]:
                return False

            # If t[i] already has a mapping,
            # it must match s[i]
            if t[i] in map_ts and map_ts[t[i]] != s[i]:
                return False

            # Save the mapping in both directions
            map_st[s[i]] = t[i]
            map_ts[t[i]] = s[i]

        # All characters follow a consistent one-to-one mapping
        return True


# Test the solution
solution = Solution()

print(solution.isIsomorphic("egg", "add"))     # True
print(solution.isIsomorphic("foo", "bar"))     # False
print(solution.isIsomorphic("paper", "title")) # True
