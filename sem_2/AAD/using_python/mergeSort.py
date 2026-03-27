import random
import time
import matplotlib.pyplot as plt

def generate_random(n):
    return [random.randint(1,1000) for _ in range(n)]

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


sizes = []
actual_times = []
theoretical_times = []

for n in range(100, 10001, 500):
    arr = generate_random(n)

    start = time.perf_counter()
    merge_sort(arr)
    end = time.perf_counter()

    time_taken = end - start
    theoretical_time = (n * (n.bit_length())) * 1e-7   # approx n log n

    sizes.append(n)
    actual_times.append(time_taken)
    theoretical_times.append(theoretical_time)

plt.plot(sizes, actual_times, marker='o', label="Actual Time")
plt.plot(sizes, theoretical_times, label="O(n log n)")
plt.title("Merge Sort")
plt.xlabel("Input Size")
plt.ylabel("Time")
plt.legend()
plt.grid()
plt.show()