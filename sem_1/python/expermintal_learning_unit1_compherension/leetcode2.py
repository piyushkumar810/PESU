
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


# --------------------------------- explanation ----------------------------
'''
🔸 i = 0
shortest_char[0] = 'f'
flower[0] = 'f' ✅
flow[0]   = 'f' ✅
flight[0]= 'f' ✅

✔ All match → continue


🔸 i = 1
shortest_char[1] = 'l'
flower[1] = 'l' ✅
flow[1]   = 'l' ✅
flight[1]= 'l' ✅

✔ All match → continue


🔸 i = 2
shortest_char[2] = 'o'
flower[2] = 'o' ✅
flow[2]   = 'o' ✅
flight[2]= 'i' ❌


🚨 Mismatch found

🔥 Code executes here
if s[i] != char:
    return shortest_char[:i]


i = 2

shortest_char[:2] → "fl"

✅ Returned result = "fl"

🧠 Meaning of shortest_char[:i]

This is string slicing:

shortest_char[:i]


👉 Take characters from index 0 to i-1

i	Result
0	""
1	"f"
2	"fl"
3	"flo"
'''