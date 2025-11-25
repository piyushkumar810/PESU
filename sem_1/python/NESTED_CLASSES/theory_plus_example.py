# 🌟 PART 1 — What is a Nested Class?

# A nested class (or inner class) is a class defined inside another class.

# Syntax:

# class Outer:
#     class Inner:
#         pass


# Think of it like:

# Class inside a class

# 🌟 PART 2 — Basic Example
# class Outer:
#     class Inner:
#         def show(self):
#             print("Inside Inner class")

# # Create object of Inner class
# inner_obj = Outer.Inner()
# inner_obj.show()


# Output:

# Inside Inner class

# 🌟 PART 3 — WHY do we use nested classes?
# ✔ To logically group classes

# When one class is only used inside another.

# ✔ To create helper classes

# Used only by the outer class.

# ✔ To prevent unnecessary exposure

# Inner class is hidden inside outer class.

# ✔ To create complex objects (like trees, linked lists)
# 🌟 PART 4 — Example: College & Student
# class College:
#     def __init__(self, name):
#         self.name = name

#     class Student:
#         def __init__(self, student_name):
#             self.student_name = student_name

#         def show(self):
#             print("Student:", self.student_name)

# # Creating object of nested class
# s = College.Student("Rahul")
# s.show()

# 🌟 PART 5 — Access inner class from outer class
# class Company:
#     class Employee:
#         def __init__(self, name):
#             self.name = name

#         def display(self):
#             print("Employee:", self.name)

# # Access using outer class
# emp = Company.Employee("John")
# emp.display()

# 🌟 PART 6 — Inner class using outer class object
# class Car:
#     def __init__(self, model):
#         self.model = model
#         self.engine = self.Engine()  # creating inner class object inside outer class

#     class Engine:
#         def start(self):
#             print("Engine started")

# c = Car("BMW")
# c.engine.start()

# 🌟 PART 7 — Realistic Example: Linked List Node inside LinkedList
# class LinkedList:

#     class Node:    # inner class
#         def __init__(self, data):
#             self.data = data
#             self.next = None

#     def __init__(self):
#         self.head = None

#     def insert(self, data):
#         new_node = self.Node(data)
#         new_node.next = self.head
#         self.head = new_node

# ll = LinkedList()
# ll.insert(10)
# ll.insert(20)


# ➡ Node class is used ONLY inside LinkedList, so nested class makes sense.

# 🌟 PART 8 — When to Use Nested Classes?

# ✔ When the inner class is not useful outside the outer class
# ✔ When you want to encapsulate some behavior
# ✔ For data structures (Node inside Tree, LinkedList, Stack)
# ✔ For GUI components (Button inside Window)
# ✔ For grouping related logic

# 🌟 PART 9 — When NOT to use nested classes?

# ❌ When classes are independent
# ❌ When inner class needs to be used everywhere
# ❌ When code becomes confusing or messy

# 🌟 PART 10 — Nested Class With Class Variables, Methods
# class A:
#     class B:
#         count = 0

#         @classmethod
#         def show_count(cls):
#             print("Count =", cls.count)

# A.B.count = 5
# A.B.show_count()