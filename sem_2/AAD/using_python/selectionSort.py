import random
import time
import matplotlib.pyplot as plt

def generate_random(n):
    return [random.randint(1,1000) for _ in range(n)]

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        min_index = i
        
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]


sizes = []
actual_times = []
theoretical_times = []

for n in range(100, 10001, 500):
    arr = generate_random(n)

    start = time.perf_counter()
    selection_sort(arr)
    end = time.perf_counter()

    time_taken = end - start
    theoretical_time = (n * n) * 1e-8   # O(n²)

    sizes.append(n)
    actual_times.append(time_taken)
    theoretical_times.append(theoretical_time)

plt.plot(sizes, actual_times, marker='o', label="Actual Time")
plt.plot(sizes, theoretical_times, label="O(n²)")
plt.title("Selection Sort")
plt.xlabel("Input Size")
plt.ylabel("Time")
plt.legend()
plt.grid()
plt.show()