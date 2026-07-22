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


'''
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

| i | arr[i] | current_sum     | max_sum |
| - | ------ | --------------- | ------- |
| 0 | -2     | -2              | -2      |
| 1 | 1      | max(1, -2+1)=1  | 1       |
| 2 | -3     | max(-3, 1-3)=-2 | 1       |
| 3 | 4      | max(4, -2+4)=4  | 4       |
| 4 | -1     | max(-1, 4-1)=3  | 4       |
| 5 | 2      | max(2, 3+2)=5   | 5       |
| 6 | 1      | max(1, 5+1)=6   | 6       |
| 7 | -5     | max(-5, 6-5)=1  | 6       |
| 8 | 4      | max(4, 1+4)=5   | 6       |

'''