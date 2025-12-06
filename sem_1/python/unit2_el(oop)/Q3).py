# Create classes
# A 
# B(A) 
# C(A) 
# D(B, C)
# Define process() in all classes, but intentionally change parameter order in some methods.
# Call process() from D.

class A:
    def process(self,x,y):
        print(f"A.processs() => x ={x} and y= {y}")

class B(A):
    # Changing parameter order intentionally
    def process(self,y,x):
        print(f"B.processs() => y ={y} and x= {x}")

class C(A):
    # Different signature: 3 parameters   
    def process(self,a,b,c=None):
        print(f"C.processs() => a ={a} , b= {b} and c={c}")

class D(B,C):
    # D overrides with its own style
    def process(self,p,q):
        print(f"D.processs() => p ={p} and q= {q} ")

obj=D()
obj.process(10,20)

print(D.mro())

# ✔ Why does D’s method run?
# Because Python follows MRO (Method Resolution Order):


'''
✔ Why change parameter order?

So you can clearly see:

B expects parameters as (y, x)
C expects (a, b, c)
A expects (x, y)
D expects (p, q)

But none matter because D overrides all of them, so its version is used first.
'''