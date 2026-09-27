# Q1
def second_largest(arr):
    if(len(arr)<2):
        return None

    else:
        largest=send_largest=float('-inf')

        for i in arr:
            if(i>largest):
                send_largest=largest
                largest=i

            elif(largest>i>send_largest):
                send_largest=i

        return send_largest

arr=[23,54,23,54,23,54,78,23,8,12,5]
print(second_largest(arr))


# Q2
def rev_array(arr):
    return arr[::-1]

arr=[23,54,23,54,23,54,78,23,8,12,5]
print(rev_array(arr))
# ---or

def rev_array(arr):
    low=0
    high=len(arr)-1

    while(low<high):
        arr[low],arr[high]=arr[high],arr[low]
        low+=1
        high-=1
    return arr

arr=[23,54,23,54,23,54,78,23,8,12,5]
print(rev_array(arr))


# Q3 
def sorted_arr(arr):
    for i in range(len(arr)-1):
        if(arr[i]>arr[i+1]):
            return "this array is not sorted"
    return "this array is perfectly sorted"

arr=[5,10,20,30,70,50]
print(sorted_arr(arr))


# 4th
def duplicy_removal(arr):
    print(set(arr))
    print(type(arr))

arr = [23, 54, 23, 54, 23, 54, 78, 23, 8, 12, 5]
print(duplicy_removal(arr))
# ---or

def duplicy_removal(arr):
    i=0
    for j in range(1,len(arr)):
        if(arr[j]!=arr[i]):
            i+=1

            arr[i]=arr[j]

    return arr[:i+1]

# arr = [23, 54, 23, 54, 23, 54, 78, 23, 8, 12, 5]
'''Your code is using the two-pointer technique, but there is one important issue: this technique works for sorted arrays when removing duplicates.'''

arr=[10,20,20,30,40,40,50,60,60]
print(duplicy_removal(arr))

