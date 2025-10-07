l1=[]
l1.append([1,[2,3],4])
l1.extend([7,8,9])
print(l1)
print(l1[0][1][1]+l1[2])

l1=[1,2,3,4]
l2=l1
l3=l1.copy()
l4=l1
l1[0]=[5]
print(l1)
print(l2)
print(l3)
print(l4)
l=[1,3,5,7,9]
print(l.pop(-3), end="*")
print(l)
print()

# -------slice assignment
alist=[4,8,12,16,18,20]
alist[1:4]=[20,24,28]
print(alist)
print()

# ---------------- deletion of list
sampleList=[10,20,30,40,50,60,70]
print(sampleList)
del sampleList[0:6]
print(sampleList)
print()

#------------- append, tuple, slicing, max over string 
alist1=(5,10,15,25)
print(alist1[:-2])
list1=["xyz", "zara", "pyhton"]
print(max(list1))
print(len([None]*10))
print()

# ------------- set and set operation
print(({1,2,3,4,5}-{3,4}^{5,6,7,3}))
x={1,2,3}
y={1,2}
print(y.issubset(x))
print(y<x)
print()

