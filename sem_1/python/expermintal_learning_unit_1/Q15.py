'''
Create three functions Functions:

is_prime(n), is_perfect(n), is_armstrong(n)
Ask user for a number and classify which types apply
'''
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
    
def is_perfect(n):
    if n<=0:
        return False
    sum_div=0
    for i in range(1,n):
        if n%i==0:
            sum_div+=i
    return sum_div==n
    
def is_armstrong(n):
    num_str=str(n)
    num_len=len(num_str)
    total=0
    for digit in num_str:
        total+=int(digit)**num_len
    return total==n
    
num=int(input("enter a number: "))

types_list=[]
if is_prime(num):
    types_list.append("prime")
if is_perfect(num):
    types_list.append("perfect")
if is_armstrong(num):
    types_list.append("Armstrong")
    
if types_list:
    print(f"the number {num} is: ", ", ".join(types_list))
else:
    print(f"the number {num} is non if prime, perfect or armstrong")