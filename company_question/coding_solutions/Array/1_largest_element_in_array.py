# 1. Find the largest element in an array

def largest(arr):
    n=len(arr)
    print(n)

    for i in range(n):
        largest=arr[i]
        for j in range(n-1):
            if(largest<arr[j+1]):
                largest=arr[j+1]
                continue

    return largest
       

arr=[10,645,94,20,30,45,200,100]
print(largest(arr))

# above code got 2/5
'''
| Criteria                  | Marks   |
| ------------------------- | ------- |
| Logic Correctness         | 1/2     |
| Time Complexity           | 0/1     |
| Readability               | 0.5/1   |
| Optimization & Edge Cases | 0.5/1   |
| **Total**                 | **2/5** |

'''

# ------------------------ best time complexity code

def LargstElement(arr1):
    if(len(arr1)==0):
        return None
    
    else:
        largest1=arr1[0]
        for i in range (len(arr1)-1):
            if(largest1<arr1[i+1]):
                largest1=arr1[i]
        
        return largest1


arr1=[10,645,94,20,30,45,200,100]
print(LargstElement(arr1))

# ------------ got 4/5


# full 5/5 code
def LargestElement(arr1):
    if len(arr1) == 0:
        return None

    largest1 = arr1[0]

    for i in range(1, len(arr1)):
        if arr1[i] > largest1:
            largest1 = arr1[i]

    return largest1


arr1 = [10,645,94,20,30,45,200,100]
print(LargestElement(arr1))