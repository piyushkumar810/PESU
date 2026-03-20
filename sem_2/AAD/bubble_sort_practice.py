import random
import time
import matplotlib.pyplot as plt

# Generate random numbers
def generate_random(n):
    return [random.randint(1,1000) for _ in range(n)]

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

sizes = []
actual_times = []
theoretical_times = []

for n in range(100, 2001, 100):
    
    arr = generate_random(n)
    
    start = time.time()
    bubble_sort(arr)
    end = time.time()
    
    actual_time = end - start
    theoretical_time = (n*n)*1e-7
    
    sizes.append(n)
    actual_times.append(actual_time)
    theoretical_times.append(theoretical_time)

# Plot Graph
plt.figure()

plt.plot(sizes, actual_times, marker='o', label="Actual Time")
plt.plot(sizes, theoretical_times, linewidth=2, label="Theoretical O(n²)")

plt.title("Bubble Sort Time Complexity")
plt.xlabel("Input Size (n)")
plt.ylabel("Time (seconds)")
plt.grid(True)
plt.legend()

plt.show()