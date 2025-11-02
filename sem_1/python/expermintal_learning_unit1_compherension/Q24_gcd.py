# Write a function to find LCM of two numbers using a helper function for GCD.

# Helper function to find GCD (Greatest Common Divisor)
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Function to find LCM using GCD
def lcm(a, b):
    return (a * b) // gcd(a, b)

# Example usage
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("LCM of", num1, "and", num2, "is:", lcm(num1, num2))
