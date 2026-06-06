def findMissingNumber(arr):
    n = len(arr)

    for i in range(n):
        if arr[i] != i + 1:
            return i + 1

    return n + 1


arr=[1,2,4,5]
print(findMissingNumber(arr))