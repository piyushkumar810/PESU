# Create a base class Person with name and age, and a subclass Student with roll number and marks.
# Display full student information using inheritance.d


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Derived class
class Student(Person):
    def __init__(self, name, age, roll, marks):
        # Calling Person class constructor
        super().__init__(name, age)
        self.roll = roll
        self.marks = marks

    def display_student(self):
        # Display Person details
        self.display_person()
        # Display Student details
        print("Roll Number:", self.roll)
        print("Marks:", self.marks)


# Creating a Student object
s = Student("Piyush", 19, 28, 92)

# Displaying full student info
s.display_student()
