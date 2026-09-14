# Power Function Using Recursion
# We want to calculate:
# xⁿ

# Example:

# 2³ = 2 × 2 × 2 = 8

def power(x, n):
    if n == 0:      # Base case
        return 1

    return x * power(x, n - 1)

print(power(2, 5))