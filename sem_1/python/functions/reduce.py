# reduce is not a built in function of python 
# if i want to use it then we have to import it 

from functools import reduce
num=[1,2,3,4]
res=reduce(lambda x,y : x+y, num)
print(res)

print()
prod=reduce(lambda x,y : x*y, num)
print(prod)

print()
print("q1. use reduce function to find out the largest value of the list ")
list1=[12,10,45,7,89,23]
largest = reduce(lambda a, b: a if a > b else b, list1)
print("The largest value in the list is:", largest)
print()

print("q2. use bith map() and reduce() to find sum of squares")
def square(lst):
    double=list(map(lambda x: x**2, lst))
    return(double)

list2=[1,2,3,4,5]
dou=square(list2)
print(dou)

add=reduce(lambda a,b : a+b, dou)
print(add)