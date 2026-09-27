def remove_zeros(arr):
    i = 0

    for j in range(len(arr)):
        if arr[j] != 0:
            arr[i] = arr[j]
            i += 1

    return arr[:i]


arr = [0, 23, 0, 54, 12, 0, 8, 0, 5]

print(remove_zeros(arr))