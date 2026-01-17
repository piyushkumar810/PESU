

def factorial(num):
    if(num==1 or num == 0):
        return 1
    n= num*factorial(num-1)
    return n

num1=(int(input("enter the number")))
print(factorial(num1))