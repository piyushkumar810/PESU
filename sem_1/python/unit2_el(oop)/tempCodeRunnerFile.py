
class parent:
    def show(self):
        print(f"hey i am from parent class ")

class child(parent):
    def show(self):
        print(f"hey i am from child class ")

obj1=child()
print(obj1.show())
print(child.mro())