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

'''
4. What happens when del obj is used?

A. Destructor always gets called
B. Destructor never gets called
C. Destructor may or may not be called
D. Python throws error

Answer: C
Explanation:
Python's garbage collector decides when to destroy the object.
'''

# --------------inheritance
class base:
    def display1(self):
        print("jello")

class child(base):
    def display2(self):
        print("hello child class")

x=child()
x.display1()
x.display2()


class prot:
    def __init__(self):
        self.__n=405
    
    def diplay(self):
        print(f"my value is private {self.__n}")

prot1=prot()
prot1.diplay()
# print(prot1.__n)  cannot access it is private