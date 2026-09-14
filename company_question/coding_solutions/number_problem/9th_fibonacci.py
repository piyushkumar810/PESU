def fibonacci(num):
    if num <= 1:
        return num

    return fibonacci(num - 1) + fibonacci(num - 2)

print(fibonacci(7))

# ------------------------ or- ----------------------------

def fibonacci(num):
    a = 0
    b = 1

    for i in range(num):
        print(a)
        a, b = b, a + b

fibonacci(7)