# 3. Reverse an array

def reverse_array(arr):
    if(len(arr)==0):
        return None
    else:
        arr=arr[ ::-1]
        return arr


arr=[1,2,3,4,5,6,7,8,9]
print(reverse_array(arr))
# ---------- got 4/5

# correct edge case
def reverse_array(arr):
    if len(arr) == 0:
        return []
    return arr[::-1]


arr=[1,2,3,4,5,6,7,8,9]
print(reverse_array(arr))

# problem
'''
Complexity
Using slicing:

arr[::-1]
Time Complexity: O(n)
Space Complexity: O(n) (creates a new reversed list)
'''


# improved code --------------- 5/5
def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr


arr=[1,2,3,4,5,6,7,8,9]
print(reverse_array(arr))