# Write a recursive function to find the nth Fibonacci number.
# Recursive function to find nth Fibonacci number
def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
n = int(input("Enter which Fibonacci term you want: "))
print(f"The {n}th Fibonacci number is:", fibonacci(n))
