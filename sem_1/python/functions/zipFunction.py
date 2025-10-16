#-------------------------------------- zip() in python--------------------------------------
a=[1,2,3,4,5]
b=['a','b','c','d','e']
zipit=list(zip(a,b))
di=dict(zip(a,b))
print(zipit)
print(di)

print()
# how to unzip the zipped list
letters,numbers=zip(*zipit)
print(letters)
print(numbers)


# ----------------- max() -----------------------
print()
# it takes lexicographic order 
print(max(12,23,45,67))
lis=['apple', 'banana', 'cherry']
print(max('apple', 'banana', 'cherry'))
# getting max value by character length
print(max(lis, key=len))


# --------------------- min() --------------------
print()
print(min(12,23,45,67))
print(min('apple', 'banana', 'cherry'))
print(min('Hello','hello','HELLO'))
