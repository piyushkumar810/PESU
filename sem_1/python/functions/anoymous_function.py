# what is anoymous function
#  a function without name , and it is created using lambda function

# syntax:- 
# lambda argument : expression

# map()
# it takes two argument iterable and callable

# lambda function or anoynomus fucntion
x=lambda a,b : a+b
print(x(5,10))
print()

# -------------------------- map()---------------------
# a=[10,20,30,40,50]
# length=list(map(len,a))
# print(length)

# take a list consisting of numbers and double it
# print()
# def double_it(x):
#     return x*2
# # print(double_it(3))

# l=[1,2,3,4]
# newl=[]
# for item in l:
#     newl.append(double_it(item))
# print(newl)

# with map function
print()
double=list(map(lambda x: x*2, [1,2,3,4]))
print(double)


# ---------------------- filter()
print()
li=[1,2,3,5,8,13]
odd=list(filter(lambda x:x%2!=0,li))
print(odd)

# string representing integer integer
# ['1','2','3'] -> [1,2,3]
print()
strInt=['1','2','3']
