# Create the following hierarchy
# Class A 
# Classes B(A), C(A) 
# Class D(B, C)
# Each has a method info().
# Call info() from an instance of D and display the MRO using D.mro().

class A:
    def info(self):
        print(f"")

class B(A):

class C(A):

class D(B,C):