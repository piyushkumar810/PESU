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





# -------------------- palindrom
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







# ----------------------------------- note
'''' 
✔ 1. / — Normal Division (Gives FLOAT)
/ always gives a decimal number (float).

Example:
10 / 3   → 3.3333333
10 / 2   → 5.0

Even if the result is a whole number, Python makes it float.



✔ 2. // — Floor Division (Gives INTEGER for positive numbers)
// removes the decimal part and gives the integer part only.

Example:
10 // 3   → 3
10 // 2   → 5

This is what we use when we want to cut off the last digit of a number.
'''