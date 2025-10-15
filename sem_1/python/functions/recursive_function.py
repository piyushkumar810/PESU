# sum of n number can be written as 

def sum(n):
    if n==0:
        return 0
    else:
        return n+sum(n-1)
n=5
print(f"sum of the first {n} number is : {sum(n)}")

# display numbers downword
print()
def countdown(n):
    if n==0:
        print('end')
    else:
        print(n)
        countdown(n-1)
countdown(5)

# factorial of a number
print()
def factorial(n1):
    if (n==0 or n1==1):
        return 1
    else:
        return n1*factorial(n1-1)
n1=5
print(f"the factorial on {n} is {factorial(n1)}")

# gcd
print()
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
print(gcd(10,2))