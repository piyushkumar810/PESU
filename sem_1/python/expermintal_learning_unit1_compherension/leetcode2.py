
#longest common prefix 
# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        shortest_char=min(strs,key=len)
        print(shortest_char)

        for i in range(len(shortest_char)):
            char=shortest_char[i]
            for s in strs:
                if s[i]!=char:
                    return shortest_char[:i]
        
        return shortest_char



s1=Solution()
strs=["piyush","piyranshu","piyu"]
print(s1.longestCommonPrefix(strs))














# def longestCommonPrefix(strs):
#     if not strs:
#         return ""

#     # Take the shortest string (prefix can't be longer than this)
#     shortest = min(strs, key=len)

#     for i in range(len(shortest)):
#         char = shortest[i]
#         for s in strs:
#             if s[i] != char:
#                 return shortest[:i]

#     return shortest
