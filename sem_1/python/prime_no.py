# find prime no between 1-50

# def prime(num):
#     i=2
#     while(i<=num/2):
#         if(num%i==0):
#             print("this is no a prime value")
#             return
#         else:
#             print(f"{num} is a prime number")
#         i+=1
#         return

# n=int(input("enter a value : "))
# prime(n)


# --------------------------- little better way
# def prime(num):
#     if num <= 1:
#         print(f"{num} is not a prime number")
#         return

#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             print(f"{num} is not a prime number")
#             return
#     print(f"{num} is a prime number")


# n = int(input("Enter a value: "))
# prime(n)


def finding_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return
    print(f"{num}")


print("prime no's between 1 to 51 are \n :")
for i in range(1,51):
    finding_prime(i)