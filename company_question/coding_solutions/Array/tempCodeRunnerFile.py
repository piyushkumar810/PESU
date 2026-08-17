def remove_duplicate(arr):
    if(len(arr)==0):
        return []
    result=[arr[0]]

    for i in range(1,len(arr)):
        if(arr[i]!=arr[i-1]):
            result.append(arr[i])
    return result


arr=[2,4,4,6,6,7,9,12,12,12,15]
print(remove_duplicate(arr))