def check_pallindrom(num):
    sum=0
    quotp=num
    while(quotp!=0):
        r=quotp%10
        sum=sum*10+r
        quotp=quotp//10

    if(num==sum):
        print(f"yes your number {sum} is an pallindrom  number")
    else:
        print(f"no this is not pellindrom number")

inptup=int(input("enter the numbur you want to check: "))
check_pallindrom(inptup)
