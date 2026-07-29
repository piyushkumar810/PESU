# Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length

s1 = Solution()

print(s1.lengthOfLongestSubstring("abcabcbb"))  
print(s1.lengthOfLongestSubstring("bbbbb"))     
print(s1.lengthOfLongestSubstring("pwwkew"))

# -------------------------------------------------------------------------------------------------
# More Efficient Version (Using Dictionary)
# Instead of removing characters one by one, store the last index of each character.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = 0
        max_length = 0

        for right, ch in enumerate(s):
            if ch in last_seen and last_seen[ch] >= left:
                left = last_seen[ch] + 1

            last_seen[ch] = right
            max_length = max(max_length, right - left + 1)

        return max_length

s1 = Solution()

print(s1.lengthOfLongestSubstring("abcabcbb"))  