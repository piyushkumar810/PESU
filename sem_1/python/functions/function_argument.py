# -------------------------------- function argument --------------------------------

# 1st --> positional argument
def printme(name,age):
    print(name, age)

printme('piyush kuamr', '22')

# 2nd --> keyword argument
print()
printme(age=30, name="piyush")

# 3rd --> default argument
print()
def default(name, age=49):
    print(name,age)

default("piyush")

# 4th --> variable length argument
print()
def multiplier(*args):
    prod=1
    for i in args:
        prod +=1
    print('product : ', prod)
multiplier('table', 'chair', 'grocery', 'shoups')

# variable length keyword argument(**kwarg)
print()
def info(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')
    print(type(info))

info(name='python', age=60, dept='mca')

# ----------------- comdinationn of all type of argument
print()
def combo(a, b=10, *args, **kwargs):
    print("a= ", a)
    print("b= ", b)
    print("args =", args)
    print("kwargs=" , kwargs)

combo(1,2,3,4,x=100,y=200)