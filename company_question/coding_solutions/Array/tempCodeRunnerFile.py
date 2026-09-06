
class Solution:
    def removing_duplicate(self, arr):
        i = 0

        for j in range(1, len(arr)):
            if arr[j] != arr[i]:
                i += 1
                arr[i] = arr[j]

        return arr[:i+1]


arr = [1,2,2,3,3,5]

obj = Solution()
print(obj.removing_duplicate(arr))