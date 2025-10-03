# ------------------------------- lists --------------------------
l=[1,"two", 3.5, [2,3,4], {2,3,5}]
print(l)
print(type(l))
print()

# printing using index
for i in l:
    print(i)
print()

# list creation
my_stirng="python"
my_list=list(my_stirng)
print(my_list)
print()

# ------------------------ funnction of lists
# 1. append()
fruite=["apple", "banana"]
fruite.append("mango")
print(fruite)
print()

# 2.insert()  -> you must include index where you want to insert
fruite.insert(1,"cherry")
print(fruite)
print()

# 3pop()
print(fruite.pop())
print(fruite)
print()

# sort()
num=[10,40,30,20,5]
num.sort()
print(num)