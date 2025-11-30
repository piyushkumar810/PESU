def check_armstrong(num):
    sum=0
    quot=num
    while(quot!=0):
        r=quot%10
        cub=r*r*r
        sum=sum+cub
        quot=quot//10
        
    if(num==sum):
        print(f"yes your number {sum} is an armstrong number")
    else:
        print(f"no this is not armstrong number")


inptu=int(input("enter the numbur you want to check: "))
check_armstrong(inptu)