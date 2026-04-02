'''
🔹 Definition:

Exhaustive search = try ALL possibilities until you find the answer

👉 No optimization
👉 No shortcut
👉 Just check everything
'''

# 🧠 2️⃣ Where it is used?
'''
Linear search (basic case)
Password cracking
Subset problems
Travelling Salesman (brute force)
'''


# algorithm
'''
Algorithm Exhaustive_Search(arr, n, key):

1. for i = 0 to n-1:
2. ```
   if arr[i] == key:
   ```
3. ```
       return i   // found at index i
   ```
4. return -1          // not found
'''

# recursive case(decision remain)
'''
-->iteration through all choices for the current decision
-->

Exhaustive search --> we will deeply use in unit 3 and 4
Exhaustive search is exponential in nature 
'''