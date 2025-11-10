from functools import reduce
num=[5, 10, 15, 20]
sum_of_all=reduce(lambda a,b:a+b , num)
print(sum_of_all)