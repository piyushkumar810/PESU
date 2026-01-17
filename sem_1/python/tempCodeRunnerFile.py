def factorial1(num):
    if(num==1 or num==0):
        return 1
    else:
        f=1
        while(num>1):
            f=f*num
            num =num-1
        return f

print(factorial1(5))