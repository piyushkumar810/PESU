# Create the following hierarchy
# Class A 
# Classes B(A), C(A) 
# Class D(B, C)
# Each has a method info().
# Call info() from an instance of D and display the MRO using D.mro().

class A:
    def info(self):
        print(f"this is from A class info method")

class B(A):
    def info(self):
        print(f"this is from B class info method")

class C(A):
    def info(self):
        print(f"this is from C class info method")

class D(B,C):
    def info(self):
        print(f"this is from D class info method")

obj=D()
obj.info()

print(D.mro())