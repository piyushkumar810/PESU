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