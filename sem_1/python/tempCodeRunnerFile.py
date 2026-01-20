def fibonacci3(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci3(n-1) + fibonacci3(n-2)

# print first 10 Fibonacci numbers
n = 10
for i in range(n):
    print(fibonacci3(i), end=" ")
