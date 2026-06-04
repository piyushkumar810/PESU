# 7. Rotate array by K positions

'''1. Left Rotate by K Positions
Example
arr = [1,2,3,4,5]
k = 2

Output:

[3,4,5,1,2]
Code
'''
def left_rotate(arr, k):
    if len(arr) == 0:
        return []

    k = k % len(arr)

    return arr[k:] + arr[:k]


arr = [1,2,3,4,5]
k = 2

print(left_rotate(arr, k))

'''
Complexity
Time Complexity: O(n)
Space Complexity: O(n)
'''

# 2. Right Rotate by K Positions
'''Example
arr = [1,2,3,4,5]
k = 2

Output:

[4,5,1,2,3]
Code
'''
def right_rotate(arr, k):
    if len(arr) == 0:
        return []

    k = k % len(arr)

    return arr[-k:] + arr[:-k]


arr = [1,2,3,4,5]
k = 2

print(right_rotate(arr, k))
'''Complexity
Time Complexity: O(n)
Space Complexity: O(n)
Interview Optimal (In-place, O(1) Space)
'''
# For 5/5 marks, learn the reversal method.

# Left Rotate
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def left_rotate(arr, k):
    n = len(arr)

    if n == 0:
        return []

    k = k % n

    reverse(arr, 0, k - 1)
    reverse(arr, k, n - 1)
    reverse(arr, 0, n - 1)

    return arr


arr = [1,2,3,4,5]
print(left_rotate(arr, 2))

# Output:
# [3,4,5,1,2]

# Right Rotate
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def right_rotate(arr, k):
    n = len(arr)

    if n == 0:
        return []

    k = k % n

    reverse(arr, 0, n - 1)
    reverse(arr, 0, k - 1)
    reverse(arr, k, n - 1)

    return arr


arr = [1,2,3,4,5]
print(right_rotate(arr, 2))
'''
Output:

[4,5,1,2,3]
Complexity
Time Complexity: O(n)
Space Complexity: O(1) ✅'''