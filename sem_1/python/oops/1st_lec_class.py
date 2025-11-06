# 🧩 1. Class
# A class is a blueprint or template that defines how an object will look and behave.


# 🚗 2. Object
# An object is an instance of a class — a real version created from that blueprint.
# Each object can have its own data.

# 🎯 3. Attributes
# Attributes are variables inside a class that hold data related to the object.
# They can be:
# Class attributes (shared by all objects)
# Instance attributes (unique to each object)


# ⚙️ 4. Methods
# Methods are functions inside a class that define the behavior of the objects.


class student:
    def __init__(self,name,course):
        self.name=name
        self.course=course

    def inntroduce(self):
        print("hello, my name is", self.name)
        print("i am studing", self.course)


s1=student("piyush", "in peoples education sociaty (PESU) ")
s1.inntroduce()