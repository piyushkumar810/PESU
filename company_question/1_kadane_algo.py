'''
Kadane's Algorithm in Python
Problem

Find the maximum sum of a contiguous subarray.

Time Complexity
O(n)
Space Complexity
O(1)
'''



def kadane(arr):
    current_sum = arr[0]
    max_sum = arr[0]

    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum Sum:", kadane(arr))