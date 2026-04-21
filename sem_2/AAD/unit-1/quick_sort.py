# choose a pivot element
# partition the array
# element smaller than pivote->left side
# element greater than pivote -> right side
# recursively apply quick sort on left and right side


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1


def quicksort_non_recursive(arr):
    size = len(arr)
    stack = []

    # push initial range
    stack.append((0, size - 1))

    while stack:
        low, high = stack.pop()

        if low < high:
            pi = partition(arr, low, high)

            # push left subarray
            stack.append((low, pi - 1))

            # push right subarray
            stack.append((pi + 1, high))


# Example
arr = [8, 3, 1, 7, 0, 10, 2]
quicksort_non_recursive(arr)
print(arr)