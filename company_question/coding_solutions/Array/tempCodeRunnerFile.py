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