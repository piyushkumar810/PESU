# 1. Maximum Element in an Array
'''
Algorithm
Algorithm MaxElement(A[0...n-1])

1. max ← A[0]
2. for i ← 1 to n-1 do
       if A[i] > max then
            max ← A[i]
3. return max
Answers
Natural size metric: n (number of elements)
Basic operation: Comparison (A[i] > max)
Basic operation count differs? No (always n-1 comparisons)
Efficiency: Θ(n)
'''


# 2. Minimum Element in an Array
'''
Algorithm
Algorithm MinElement(A[0...n-1])

1. min ← A[0]
2. for i ← 1 to n-1 do
       if A[i] < min then
            min ← A[i]
3. return min
Answers
Natural size metric: n
Basic operation: Comparison (A[i] < min)
Differs? No
Efficiency: Θ(n)
'''


# 3. Linear Search
'''
Algorithm
Algorithm LinearSearch(A,n,key)

1. for i ← 0 to n-1 do
       if A[i] == key then
            return i
2. return −1
Answers
Natural size metric: n
Basic operation: Comparison (A[i] == key)
Differs? Yes (depends on key position)
Efficiency:
Best: Θ(1)
Average: Θ(n)
Worst: Θ(n)
'''


# 4. Binary Search
'''
Algorithm
Algorithm BinarySearch(A,low,high,key)

while low ≤ high
    mid ← (low+high)/2

    if A[mid]==key
        return mid
    else if key<A[mid]
        high←mid−1
    else
        low←mid+1

return −1
Answers
Natural size metric: n
Basic operation: Comparison with middle element
Differs? Yes
Efficiency:
Best: Θ(1)
Worst: Θ(log n)
'''


# 5. Bubble Sort
'''
Algorithm
Algorithm BubbleSort(A,n)

for i←0 to n-2
    for j←0 to n-2-i
        if A[j]>A[j+1]
            swap
Answers
Natural size metric: n
Basic operation: Comparison
Differs? Yes (optimized version)
Efficiency:
Worst: Θ(n²)
'''


# 6. Selection Sort
'''
Algorithm
Algorithm SelectionSort(A,n)

for i←0 to n-2
    min=i
    for j←i+1 to n-1
        if A[j]<A[min]
             min=j
    swap
Answers
Natural size metric: n
Basic operation: Comparison
Differs? No
Efficiency: Θ(n²)
'''


# 7. Insertion Sort
'''
Algorithm
Algorithm InsertionSort(A,n)

for i←1 to n-1
    key=A[i]
    j=i-1

    while j>=0 and A[j]>key
        A[j+1]=A[j]
        j--

    A[j+1]=key
Answers
Natural size metric: n
Basic operation: Comparison
Differs? Yes
Efficiency:
Best: Θ(n)
Worst: Θ(n²)
'''


# 8. Unique Elements
'''
Algorithm
Algorithm Unique(A,n)

for i←0 to n-2
    for j←i+1 to n-1
        if A[i]==A[j]
             return False

return True
Answers
Natural size metric: n
Basic operation: Comparison
Differs? Yes
Efficiency:
Best: Θ(1)
Worst: Θ(n²)
'''

# 9. Matrix Multiplication
'''
Algorithm
Algorithm MatrixMultiply(A,B,C)

for i←0 to n-1
    for j←0 to n-1
        C[i][j]=0
        for k←0 to n-1
            C[i][j]+=A[i][k]*B[k][j]
Answers
Natural size metric: n
Basic operation: Multiplication
Differs? No
Efficiency: Θ(n³)
'''


# 10. Count Array Elements
'''
Algorithm
Algorithm Count(A,n)

count=0

for i←0 to n-1
    count++
Answers
Natural size metric: n
Basic operation: Increment
Differs? No
Efficiency: Θ(n)
'''


# 11. Sum of Array
'''
Algorithm
Algorithm Sum(A,n)

sum=0

for i←0 to n-1
    sum=sum+A[i]

return sum
Answers
Natural size metric: n
Basic operation: Addition
Differs? No
Efficiency: Θ(n)
'''


# 12. Find Average
'''
Algorithm
Algorithm Average(A,n)

sum=0

for i←0 to n-1
     sum+=A[i]

avg=sum/n

return avg
Answers
Natural size metric: n
Basic operation: Addition
Differs? No
Efficiency: Θ(n)
'''


# 13. Count Even Numbers
'''
Algorithm
Algorithm CountEven(A,n)

count=0

for i←0 to n-1
    if A[i]%2==0
        count++

return count
Answers
Natural size metric: n
Basic operation: Modulus comparison
Differs? No
Efficiency: Θ(n)
'''


# 14. Reverse an Array
'''
Algorithm
Algorithm Reverse(A,n)

i=0
j=n-1

while i<j
    swap(A[i],A[j])
    i++
    j--
Answers
Natural size metric: n
Basic operation: Swap
Differs? No
Efficiency: Θ(n)
'''

# 15. Find Largest and Smallest Together
'''
Algorithm
Algorithm MaxMin(A,n)

max=A[0]
min=A[0]

for i←1 to n-1

    if A[i]>max
        max=A[i]

    if A[i]<min
        min=A[i]

return(max,min)
Answers
Natural size metric: n
Basic operation: Comparison
Differs? No
Efficiency: Θ(n)
'''