def factorial(n):
    if(n==1):
        return n
    else:
        return n*factorial(n-1)

n=int(input("enter the number: "))
print(factorial(n))