# You pick one element
# Compare it with previous elements
# Insert it at the correct position

'''
🔁 Step-by-Step Example

Array: [5, 3, 4, 1]

Start from 2nd element (3)
Compare with 5 → shift 5 → insert 3
→ [3, 5, 4, 1]
Take 4 → compare with 5 → shift → insert
→ [3, 4, 5, 1]
Take 1 → shift all → insert at beginning
→ [1, 3, 4, 5]
'''

def insertion_sort(arr):
    n=len(arr)

    for i in range(n):
        for j in range(i+1,n-1):
            if(arr[j]<arr[i]):
                arr[i],arr[j]=arr[j],arr[i]
                



arr=[4,6,2,1,7,2]
print(insertion_sort(arr))