# 8. Find missing number in an array
'''
Problem Statement
You are given an array containing numbers from 1 to N.
Exactly one number is missing from the array.
Find the missing number.

eg: -
arr = [1, 2, 4, 5]
3 is missing
'''

def findMissingNumber(arr):
    n=len(arr)

    for i in range(n):
        j=i+1
        if(j != arr[i]):
            return j


arr=[1,2,4,5]
print(findMissingNumber(arr))

# bad code many test case not passed
'''
| Criteria          | Marks     |
| ----------------- | --------- |
| Logic Correctness | 1/2       |
| Time Complexity   | 1/1       |
| Readability       | 0.5/1     |
| Edge Cases        | 0/1       |
| **Total**         | **2.5/5** |


test cases:
Test Case 2 (Missing Last Number) -> your code fails
Test Case 3 (Unsorted Array) -> your code fails
'''

# ---------------- better approach
def findMissingNumber(arr):
    n = len(arr)

    for i in range(n):
        if arr[i] != i + 1:
            return i + 1

    return n + 1


arr=[1,2,4,5]
print(findMissingNumber(arr))


# ---------------- interview chioce
def findMissingNumber(arr, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)

    return expected_sum - actual_sum


arr=[1,2,4,5]
n=len(arr)
print(findMissingNumber(arr,n))