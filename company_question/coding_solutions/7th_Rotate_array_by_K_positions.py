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


# ----------------------------------- explanation
'''
LEFT ROTATE ARRAY BY K POSITIONS

Example
arr = [1, 2, 3, 4, 5]
k = 2

Expected Output:
[3, 4, 5, 1, 2]

# Step 1: Original Array

arr = [1, 2, 3, 4, 5]

Index:   0   1   2   3   4
Array:  [1,  2,  3,  4,  5]


# Step 2: Calculate k
k = k % len(arr)

Here:
k = 2 % 5

Output:
2

Why do we do this?

Suppose:
k = 7
Array length = 5

Then:
k = 7 % 5
k = 2

So rotating 7 times is the same as rotating 2 times.



# Step 3: Understand arr[k:]

arr[k:]
arr[2:]

Means:
Start from index 2 and go till the end.

Index:   0   1   2   3   4
Array:  [1,  2,  3,  4,  5]


         ↓

Take all elements from index 2 onwards:
[3, 4, 5]

Therefore:
arr[k:]
becomes
[3, 4, 5]



# Step 4: Understand arr[:k]
arr[:k]
arr[:2]

Means:
Start from beginning and stop before index 2.

Index:   0   1   2   3   4
Array:  [1,  2,  3,  4,  5]

Take elements before index 2:
[1, 2]

Therefore:
arr[:k]
becomes
[1, 2]



# Step 5: Join Both Parts

arr[k:] + arr[:k]
Substitute values:
[3, 4, 5] + [1, 2]

Result:
[3, 4, 5, 1, 2]

Visual Representation

Original Array:
[1, 2 | 3, 4, 5]
After Left Rotation by 2:
[3, 4, 5 | 1, 2]

The first k elements move to the end.
Complete Code

def left_rotate(arr, k):
if len(arr) == 0:
return []

```
k = k % len(arr)

return arr[k:] + arr[:k]
```

arr = [1, 2, 3, 4, 5]
k = 2

print(left_rotate(arr, k))

Output:

[3, 4, 5, 1, 2]

Another Example

arr = [10, 20, 30, 40, 50]
k = 3

Step 1

arr[k:]

arr[3:]

Output:

[40, 50]

Step 2

arr[:k]

arr[:3]

Output:

[10, 20, 30]

Step 3

Join both parts:

[40, 50] + [10, 20, 30]

Output:

[40, 50, 10, 20, 30]

Complexity

Time Complexity: O(n)

Space Complexity: O(n)

'''