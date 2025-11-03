str="programmingwithpython"
print(str[1:3])
print()  #ro

var="james"*2*3
print(var)
print()  #

x=36/4*(3+2)*4+2
print(x)
print()

v1,v2,v3=1,2,"3"
# print(v1+v2+v3)
print()  #  unsupported operand type(s) for +: 'int' and 'str'

x1=2*2**3
print(x1)
print()

tup=(1,2,3)
print(2*tup)
print()

print((2**2)**(2**3))
print()

print(format("python programming","^30"))
print()

print(10<20 and 30<20 or 40>10)
print()

s="foo"
t="bar"
print("barf" in 2*(s+t))
print()

print(0.1+0.2 == 0.3) 
print()

# ---------------------- string slicing--------------------
s="programmingwithpython"
print(s[::5])
print(s[::-5])
print(s[0]+s[-1])
print(s[::-1][-1]+s[len(s)-1])
print(s[::-1][::-5])
# print(s[::-1])
# print(s[::-5])
print()

s1="$100 $200 $300"
print(s1.count("$"))
print(s1.count("$",5,10))
print(s1.count("$",5))
print()

# ---------------- nested list-----------------
x2=["a", ["bb", ["ccc","ddd"], "ee", "ff"], "g",["hh", "i"], "i"]
print(x2[1][1][0])
print(x2[4][0])
print(x2[1][2][1])
print(x2[2][0])
print(x2[3][1])
print()

# ------------------- list slicing --------------------
namelist=["harsh", "pratik", "bob",  "dhruv"]
print(namelist[1][-1])
l=[1,2,3,4]
l.append(5)
print(l)
list1=range(100,110)
print(list1)
print(list1.index(105))
list1=[1,2,3,4,5]
list2=list1
list2[0]=0
print(list1)
print()

# note
'''
# what does range() do ?
The range() function creates a sequence of numbers — but it doesn’t 
actually store all the numbers in memory like a list does.

here, you are printing list1
output :- range(100, 110)
That's because range() doesn't display the numbers by itself — 
it,s a special type of object.

To see the actual numbers, you can convert it to a list:
print(list(list1))
output:- [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]

'''

# ------------------------ concatination with list
list3=[2000,2002]
list4=[2024,2026]
print((list3+list4)*2)
list5=['physics','chemistry', 2000,2024]
print(list5[1][-1])
list6=[1,2,3,None,(1,2,3,4,5),["pyhton",'for','practice']]
print(len(list6))