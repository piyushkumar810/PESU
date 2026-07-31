def is_armstrong(n):
    num_digits = len(str(n))
    original = n
    total = 0

    while n > 0:
        digit = n % 10
        total += digit ** num_digits
        n //= 10

    return total == original


# Example
n = int(input("Enter a number: "))

if is_armstrong(n):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")