# largets element
def largest_element(arr):
    if(len(arr)<1):
        return None

    largest=arr[0]
    for i in range(1,len(arr)):
        if(largest<arr[i]):
            largest=arr[i]
    return largest

arr=[2,4,34,45,56,23]
print(largest_element(arr))


# 2nd largets element 
def second_largest(arr):
    if(len(arr)<2):
        return None

    largest=second_lar=float("-inf")
    for i in arr:
        if(largest<i):
            second_lar=largest
            largest=i
        elif(largest>i>second_lar):
            second_lar=i
    return second_lar

arr=[2,4,34,45,56,23]
print(second_largest(arr))

# remove duplicate from sorted array
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