# it comes under brute force paradigm
# compair adjacent element and if they are in wrong order swap them


def bubble_sort(arr):
    n=len(arr)

    for i in range(n-1):
        for j in range(n-i-1):
            if(arr[j+1]<arr[j]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

arr=[32,54,23,54,12,2,8,4,20]
print(bubble_sort(arr))