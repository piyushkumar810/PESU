# two sum

# input=[1,3,5,7] , target=6
# index=3

# def find_index(list,target):
#     count=0
#     for i in list:
#         if(i<=target):
#             count=count+1
        
#     return count

# list1=[1,3,5,7]
# print(find_index(list1,6))


# ---------------------------- best way with O(lon(n))
class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i

'''
What does enumerate() do?

enumerate() returns both the index and the value of each item while looping over a sequence.

eg:-
nums = [10, 20, 30]
for i, num in enumerate(nums):
    print(i, num)


0 10
1 20
2 30
'''

