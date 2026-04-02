def linear_search(arr, search_val):
    n = len(arr)
    
    for i in range(n):
        if arr[i] == search_val:   # ✅ correct comparison
            return i               # return index
    
    return -1   # if not found


arr = [10, 20, 30, 40, 5, 2, 12, 43, 65, 80]

result = linear_search(arr, 5)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")