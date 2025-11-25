# 🌟 What is Inheritance? (Simple Definition)
# ✅ Definition

# Inheritance is an OOP mechanism where one class (child) acquires
# the properties & methods of another class (parent).

# ✔ Why use inheritance?

# Code reusability

# Method overriding

# Extending existing classes

# Avoid duplicating code

# 🌈 Types of Inheritance in Python

# Python supports:

# Single Inheritance

# Multilevel Inheritance

# Hierarchical Inheritance

# Multiple Inheritance

# Hybrid Inheritance (combination)

# 💠 1. Single Inheritance

# One parent → One child

# A
# └── B

# ✔ Example:
# class Animal:
#     def sound(self):
#         return "Some sound"

# class Dog(Animal):   # Single inheritance
#     def bark(self):
#         return "Woof!"

# d = Dog()
# print(d.sound())
# print(d.bark())

# 💠 2. Multilevel Inheritance

# Parent → Child → Grandchild

# A
# └── B
#      └── C

# ✔ Example:
# class A:
#     def method_A(self):
#         return "Method A"

# class B(A):
#     def method_B(self):
#         return "Method B"

# class C(B):
#     def method_C(self):
#         return "Method C"

# c = C()
# print(c.method_A())
# print(c.method_B())
# print(c.method_C())

# 💠 3. Hierarchical Inheritance

# One parent → multiple children

#       A
#     / | \
#    B  C  D

# ✔ Example:
# class Parent:
#     def show(self):
#         return "Parent method"

# class Child1(Parent):
#     def c1(self):
#         return "Child1 method"

# class Child2(Parent):
#     def c2(self):
#         return "Child2 method"

# p = Child1()
# print(p.show())     # From Parent

# 💠 4. Multiple Inheritance

# One child → multiple parents

# A     B
#  \   /
#    C

# ✔ Example:
# class Father:
#     def skill1(self):
#         return "Driving"

# class Mother:
#     def skill2(self):
#         return "Cooking"

# class Child(Father, Mother):
#     pass

# c = Child()
# print(c.skill1())
# print(c.skill2())

# 💠 5. Hybrid Inheritance

# Combination of 2 or more types
# (Using multiple + hierarchical or multilevel)

# Example structure:

#       A
#      / \
#     B   C
#      \ /
#       D

# ✔ Example:
# class A:
#     def show_A(self):
#         return "A"

# class B(A):
#     def show_B(self):
#         return "B"

# class C(A):
#     def show_C(self):
#         return "C"

# class D(B, C):   # Hybrid (uses multiple + hierarchical)
#     pass

# d = D()
# print(d.show_A())

# 🔥 EXTRA IMPORTANT: MRO (Method Resolution Order)

# For Multiple/Hybrid inheritance:

# print(D.mro())


# Python uses C3 Linearization to determine method lookup order.

# 🧠 Summary Table
# Type	Structure	Meaning
# Single	A → B	One parent, one child
# Multilevel	A → B → C	Chain of inheritance
# Hierarchical	A → B, C	One parent, many children
# Multiple	A,B → C	Child inherits from multiple parents
# Hybrid	Mix of above	Complex combination