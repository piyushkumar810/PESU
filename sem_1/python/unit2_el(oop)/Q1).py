# Create a base class Parent and a derived class Child.
# Each class should have a method show().
# Call show() using a Child object and print the MRO using Child.mro().

class parent:
    def show(self):
        print(f"hey i am from parent class ")

class child(parent):
    def show(seelf):
        print(f"hey i am from child class ")

obj1=child()
print(obj1.show())
print(child.mro())