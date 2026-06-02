def removing_duplicate(arr):
    if len(arr) == 0:
        return []

    result = [arr[0]]

    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            result.append(arr[i])

    return result


arr = [10,20,20,30,30,40,50,50]
print(removing_duplicate(arr))