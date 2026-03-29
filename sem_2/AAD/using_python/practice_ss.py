def selection_sort(arr):
    n=len(arr)
    for i in range(0,n-1):
        min=i
        for j in range(i+1,n):
            if(arr[j]<arr[min]):
                min=j
        arr[i],arr[min]=arr[min],arr[i]
    return arr

arr=[60,20,30,90,10,5,7,2]
print(selection_sort(arr))