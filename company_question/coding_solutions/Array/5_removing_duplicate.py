# 5. Remove duplicates from a sorted array

# i will do it int set and then set into list so my duplicates are removed
arr = [10,20,20,30,30,40,50,50]
result=list(set(arr))
print(result)

# you can do but this is not the way to solve 
# 1st problem sorted become un sorted and because of set answer keep on changing


# ------------------------ correct code
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