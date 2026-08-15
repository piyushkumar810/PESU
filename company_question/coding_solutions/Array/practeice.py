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
    if(len(arr)<1):
        return None

    largest=second_lar=float("-inf")
    for i in arr:
        if(largest<i):
            largest=i
            second_lar=largest
        elif(largest)

arr=[2,4,34,45,56,23]
print(largest_element(arr))