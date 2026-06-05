def left_rotate(arr, k):
    if len(arr) == 0:
        return []

    k = k % len(arr)

    return arr[k:] + arr[:k]


arr = [1,2,3,4,5]
k = 2

print(left_rotate(arr, k))