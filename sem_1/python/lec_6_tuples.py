# working with tuple
num=(1,"piyush",34.5)
print(num)
print(type(num))
# where do use tuple 
# banck account details, where we do not want changes

print()
t5=1,2,3
print(t5)
print(type(t5))

# slicing in tuple
print()
my_tup=("apple", "mango", "orange", "banana")
print(type(my_tup))
print(my_tup[-1])
print(my_tup[1:4])
print(my_tup[ :4])

# tuple packing and unpacking
# packing -> means assigning multiple values into a tuple
# unpacking-> extracting values back into variable
print()
t=(10,20,30)
a,b,c=t
print(a,b,c)
print(a)
print(b)
print(c)