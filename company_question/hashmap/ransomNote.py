
"""
Question: LeetCode 383 - Ransom Note

Given two strings, ransomNote and magazine, return True
if ransomNote can be constructed using letters from magazine.
Otherwise, return False.

Each letter in magazine can only be used once.

Example:
ransomNote = "aa"
magazine = "aab"

Output: True
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = {}

        # Count the frequency of every letter in magazine
        for ch in magazine:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        # Check whether ransomNote can be constructed
        for ch in ransomNote:
            if ch not in freq or freq[ch] == 0:
                return False

            # Use one available copy of this letter
            freq[ch] -= 1

        return True


# Example 1
ransomNote = "aa"
magazine = "aab"

solution = Solution()
print(solution.canConstruct(ransomNote, magazine))

# Output: True


# Example 2
ransomNote = "aa"
magazine = "ab"

print(solution.canConstruct(ransomNote, magazine))

# Output: False
