# ---------------------- algorithm

# compute n! recursively
# input: non-ngative integer.
# output: the vvalue of n!
# if n=0 return 1
# else return factorial(n-1)*n

# --------------------- code with recursion
def fact(n):
    if n==0 or n<0:
        return 1
    else:
        return n*fact(n-1)

n=int(input("enter any number: "))
print(f"so the factorial of {n} is : {fact(n)}")


# ----------------------- without recursion
