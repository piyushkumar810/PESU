# 2. Find the second largest element
def second_largest_element(arr):
    if len(arr) < 2:
        return None

    largest = second_largest = float('-inf')

    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif largest > num > second_largest:
            second_largest = num

    return None if second_largest == float('-inf') else second_largest


arr = [100, 20, 30, 40, 12440, 23, 345, 2, 346]
print(second_largest_element(arr))





















# finding 2nd largest
def second_largest(arr):
    if(len(arr)<2):
        return None
    
    largest=second_lar=float('-inf')

    for i in arr:
        if(i>largest):
            second_lar=largest
            largest=i
        elif(largest>i>second_lar):
            second_lar=i

    return second_lar

arr=[10,32,293,498,2983,9334,-20,239]
print(second_largest(arr))


# ------------------- note
'''
For interview questions like largest element or second largest element, using arr[0] is often easier to understand for beginners.

float('-inf') → Negative Infinity
float('inf') → Positive Infinity

These are commonly used in algorithms involving maximum/minimum values.
'''