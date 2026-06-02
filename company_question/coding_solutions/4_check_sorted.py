# 4. Check if an array is sorted


def check_sorted(arr):
    if(len(arr)==0):
        return []
    else:
        for i in range(len(arr)-1):
            if(arr[i]>arr[i+1]):
                return False
        return True


arr1=[10,30,20,10,34,54,223,23]
arr2=[10,20,30,40,50,60,70,80]
print(check_sorted(arr1))
print(check_sorted(arr2))