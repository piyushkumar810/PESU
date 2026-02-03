# Create a base class Parent and a derived class Child.
# Each class should have a method show().
# Call show() using a Child object and print the MRO using Child.mro().
class Parent:
    def show(self):
        print("hey i am from parent class")


class Child(Parent):
    def show(self):
        print("hey i am from child class")


obj = Child()
obj.show()

print(Child.mro())
