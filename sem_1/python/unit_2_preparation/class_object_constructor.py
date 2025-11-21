class A:
    x = 10

obj1 = A()
obj2 = A()
obj1.x = 20
print(obj2.x)

'''
A. 10
B. 20
C. Error
D. None

Answer: A
Explanation:
x is a class variable.
obj1.x = 20 creates instance variable x only for obj1, not obj2.
'''

