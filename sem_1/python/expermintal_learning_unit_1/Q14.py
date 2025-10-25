'''
Define unique_list(nums) that returns a list with duplicates removed (preserving order).
'''

def unique_list(nums):
    unique_nums=[]
    for n in nums:
        if n not in unique_nums:
            unique_nums.append(n)
    return unique_nums
    
number_list=[1,2,2,3,4,3,6,1]
result=unique_list(number_list)
print("unique list is: ", result)