def move_all_zeros(arr):
    j=0
    for i in range(len(arr)):
        if(arr[i]!=0):
            arr[j],arr[i]=arr[i],arr[j]
            j+=1
    return arr

arr=[2,4,0,6,0,7,9,12,0,0,15,0]
print(move_all_zeros(arr))
