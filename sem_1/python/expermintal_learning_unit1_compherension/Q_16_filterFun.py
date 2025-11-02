# Use filter() with a lambda to select prime numbers from a given list.
# Given list
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# Use filter() with lambda to find primes
primes = list(filter(lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1)), numbers))

print(primes)
