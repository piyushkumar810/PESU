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

with open("bubble_time.txt", "w") as fp:
    for n in range(100, 10001, 500):
        arr = generate_random(n)

        start = time.perf_counter()  # records a high-precision timestamp
        bubble_sort(arr)
        end = time.perf_counter()    # records a high-precision timestamp

        time_taken = end - start
        theoretical_time = (n * n) * 1e-8   # 1e-8 is 0.00000001

        fp.write(f"{n} {time_taken} {theoretical_time}\n")

        sizes.append(n)
        actual_times.append(time_taken)
        theoretical_times.append(theoretical_time)


# Plot Graph
plt.figure(figsize=(10,6))

plt.plot(sizes, actual_times, marker='o', label="Actual Time")  # A circle is drawn at each point
plt.plot(sizes, theoretical_times, linewidth=2, label="Theoretical O(n²)")

plt.title("Bubble Sort Time Efficiency")
plt.xlabel("Input Size")
plt.ylabel("Time (seconds)")
plt.grid(True)
plt.legend()

plt.show()