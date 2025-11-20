# 🟦 1. Inheritance (IS–A Relationship)

# One class inherits from another.
# Child class automatically gets parent’s properties and methods.

# ✅ Python Example
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):   # Dog IS-A Animal
    def bark(self):
        print("Dog barks")

d = Dog()
d.sound()   # Inherited from Animal
d.bark()    # Dog's own method



# 🟩 2. Composition (HAS–A Relationship: Strong Ownership)

# One class contains another class.
# The contained object cannot exist without the main class.

# ✅ Python Example
class Engine:
    def start(self):
        print("Engine started")

class Car:               # Car HAS-A Engine
    def __init__(self):
        self.engine = Engine()  # Strong ownership

    def start_car(self):
        self.engine.start()

c = Car()
c.start_car()


# 📌 Here:

# Car creates Engine inside __init__

# If Car is destroyed → Engine is also destroyed
# (Strong relationship)



# 🟨 3. Aggregation (HAS–A Relationship: Weak Ownership)

# One class uses another class, but does not own it.
# The object can exist independently.

# ✅ Python Example
class Student:
    def __init__(self, name):
        self.name = name

class Teacher:               # Teacher HAS-A Student (weak)
    def __init__(self, student):
        self.student = student

s = Student("Amit")
t = Teacher(s)


# 📌 Here:
# Student exists before Teacher
# Student can live even if Teacher is deleted
# Teacher only refers to the student object
# (Weak relationship)


'''
# ⭐ FINAL SUMMARY

# Concept	                            Meaning	Python Representation
# Inheritance   IS-A	                Class Dog(Animal)
# Composition	Strong HAS-A	        Class creates its own object (Engine())
# Aggregation	Weak HAS-A	            Class receives object from outside
'''