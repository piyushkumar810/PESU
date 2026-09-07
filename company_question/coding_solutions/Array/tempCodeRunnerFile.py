
def product(arr):
    answer = [1] * len(arr)

    for i in range(len(arr)):
        product = 1

        for j in range(len(arr)):
            if i != j:
                product *= arr[j]

        answer[i] = product

    return answer


arr = [1, 2, 3, 4]

print(product(arr))