# it also comes under brute force paradigm
# it divides array into two parts sorted and unsorted part
# finds smallest element from unsorted part 
# swap it with 1st element 
# add it to sorted part

def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if(arr[j]<arr[min]):
                min=j
        arr[i],arr[min]=arr[min],arr[i]
    return arr


arr=[25,78,75,43,23,21,1,10,12]
print(selection_sort(arr))