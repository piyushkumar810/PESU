import random
import time
import matplotlib.pyplot as plt

def generate_random(n):
    return [random.randint(1,1000) for _ in range(n)]

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr)//2]
    
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)


sizes = []
actual_times = []
theoretical_times = []

for n in range(100, 10001, 500):
    arr = generate_random(n)

    start = time.perf_counter()
    arr = quick_sort(arr)
    end = time.perf_counter()

    time_taken = end - start
    theoretical_time = (n * (n.bit_length())) * 1e-7   # approx n log n

    sizes.append(n)
    actual_times.append(time_taken)
    theoretical_times.append(theoretical_time)

plt.plot(sizes, actual_times, marker='o', label="Actual Time")
plt.plot(sizes, theoretical_times, label="O(n log n)")
plt.title("Quick Sort")
plt.xlabel("Input Size")
plt.ylabel("Time")
plt.legend()
plt.grid()
plt.show()