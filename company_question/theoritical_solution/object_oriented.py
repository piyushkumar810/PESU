# What is OOP?

'''
OOP (Object-Oriented Programming) is a programming paradigm where a program is designed using classes and objects.

The main principles of OOP are:

1. Encapsulation – wrapping data and methods together.
2. Inheritance – acquiring properties and methods from another class.
3. Polymorphism – one interface, many forms.
4. Abstraction – hiding implementation details and showing only essential features.

Example:
class Car:
def start(self):
print("Car started")

car = Car()
car.start()
'''


# Class vs Object

'''
A class is a blueprint or template used to create objects.

An object is an instance of a class that represents a real entity and has its own data and behavior.

Example:
class Student:
def **init**(self, name):
self.name = name

student1 = Student("Piyush")

Here:

* Student is the class.
* student1 is the object.
* name is an instance variable.

Interview Answer:
"Class is a blueprint, whereas an object is an instance of that class."
'''

# Constructor

'''
A constructor is a special method that is automatically called when an object is created.

In Python, **init**() is commonly used as the constructor.

Example:
class Student:
def **init**(self, name, age):
self.name = name
self.age = age

student = Student("Piyush", 23)

When Student() is called, **init**() automatically initializes the object's data.

Interview Answer:
"In Python, **init**() is used as the constructor to initialize an object's attributes when the object is created."
'''

# Encapsulation ⭐

'''
Encapsulation means bundling data and methods together inside a class and controlling access to the data.

Python does not have strict private variables like some languages, but it provides naming conventions.

Example:
class BankAccount:
def **init**(self, balance):
self.__balance = balance

```
def get_balance(self):
    return self.__balance
```

account = BankAccount(5000)

print(account.get_balance())

Here, __balance is treated as a private attribute.

Interview Answer:
"Encapsulation is the process of wrapping data and methods into a single unit and restricting direct access to internal data."

Benefit:

* Data protection
* Controlled access
* Better maintainability
  '''

# Inheritance ⭐

'''
Inheritance allows one class to acquire the properties and methods of another class.

The existing class is called the parent/base class.
The new class is called the child/derived class.

Example:
class Animal:
def speak(self):
print("Animal makes sound")

class Dog(Animal):
def bark(self):
print("Dog barks")

dog = Dog()

dog.speak()
dog.bark()

Dog inherits speak() from Animal.

Interview Answer:
"Inheritance allows a child class to reuse and extend the properties and methods of a parent class."

Common types:

* Single inheritance
* Multiple inheritance
* Multilevel inheritance
* Hierarchical inheritance
* Hybrid inheritance
  '''

# Polymorphism ⭐

'''
Polymorphism means "many forms".

It allows the same method or interface to behave differently depending on the object.

Example:
class Dog:
def sound(self):
print("Bark")

class Cat:
def sound(self):
print("Meow")

def make_sound(animal):
animal.sound()

make_sound(Dog())
make_sound(Cat())

The same sound() method behaves differently for Dog and Cat.

Interview Answer:
"Polymorphism allows the same interface or method name to perform different behaviors depending on the object."

Python mainly achieves polymorphism through:

* Method overriding
* Duck typing
* Operator overloading
  '''

# Abstraction ⭐

'''
Abstraction means hiding unnecessary implementation details and exposing only the required functionality.

Python provides abstraction using the abc module and abstract base classes.

Example:
from abc import ABC, abstractmethod

class Animal(ABC):

```
@abstractmethod
def sound(self):
    pass
```

class Dog(Animal):
def sound(self):
print("Bark")

dog = Dog()
dog.sound()

The user only needs to know that sound() exists.
The internal implementation is provided by Dog.

Interview Answer:
"Abstraction hides implementation details and exposes only the essential functionality to the user."

Example from real life:
When we drive a car, we use the steering wheel and pedals without knowing the internal engine implementation.
'''

# Method Overloading

'''
Method overloading means having multiple methods with the same name but different parameters.

Python does not support traditional method overloading like Java or C++.

If we define the same method multiple times, the latest definition replaces the previous one.

However, we can achieve similar behavior using default arguments or *args.

Example:
class Calculator:
def add(self, a, b=0, c=0):
return a + b + c

calc = Calculator()

print(calc.add(10, 20))
print(calc.add(10, 20, 30))

Interview Answer:
"Python does not support traditional method overloading. We can achieve similar behavior using default arguments, *args, or other techniques."
'''

# Method Overriding

'''
Method overriding occurs when a child class provides its own implementation of a method that already exists in the parent class.

Example:
class Animal:
def sound(self):
print("Animal sound")

class Dog(Animal):
def sound(self):
print("Bark")

dog = Dog()
dog.sound()

The Dog class overrides the sound() method of Animal.

Interview Answer:
"Method overriding occurs when a child class provides a different implementation of a method inherited from its parent class."

Method overriding is an important way to achieve runtime polymorphism.
'''

# Access Specifiers

'''
Access specifiers control how class members are accessed.

Python has three commonly discussed levels:

1. Public

2. Protected

3. Private

4. Public:
   Can be accessed from anywhere.

Example:
class Student:
def **init**(self):
self.name = "Piyush"

student = Student()
print(student.name)

2. Protected:
   Written using a single underscore _.
   It is a convention indicating that the member should not be accessed directly outside the class/subclass.

Example:
class Student:
def **init**(self):
self._age = 23

3. Private:
   Written using double underscore __.
   Python uses name mangling to make direct access harder.

Example:
class Student:
def **init**(self):
self.__marks = 90

Interview Answer:
"Python does not enforce access modifiers strictly like Java. It uses naming conventions: public members have no underscore, protected members use one underscore, and private members use two underscores."
'''

# Static Variables

'''
A static variable, commonly called a class variable in Python, is shared by all objects of a class.

It is defined inside the class but outside instance methods.

Example:
class Student:
college = "PES University"

```
def __init__(self, name):
    self.name = name
```

s1 = Student("Piyush")
s2 = Student("Rahul")

print(s1.college)
print(s2.college)

Both objects share the same college variable.

Interview Answer:
"A class variable is shared among all objects of a class, whereas an instance variable belongs to a particular object."
'''

# Instance Variables

'''
An instance variable belongs to a particular object.

It is usually created using self inside the constructor.

Example:
class Student:
def **init**(self, name, age):
self.name = name
self.age = age

s1 = Student("Piyush", 23)
s2 = Student("Rahul", 22)

Here:

* s1.name and s1.age belong to s1.
* s2.name and s2.age belong to s2.

Interview Answer:
"An instance variable stores data specific to an individual object and is generally accessed using self."
'''

# Association

'''
Association represents a general relationship between two independent classes.

Both objects can exist independently.

Example:
class Teacher:
pass

class Student:
pass

teacher = Teacher()
student = Student()

A teacher teaches a student.

The Teacher and Student objects can exist independently.

Interview Answer:
"Association represents a relationship between two independent objects where neither object necessarily owns the other."

Example:
Teacher ---- teaches ---- Student
'''

# Aggregation

'''
Aggregation is a weak "has-a" relationship.

One class contains or uses objects of another class, but the contained object can exist independently.

Example:
class Student:
def **init**(self, name):
self.name = name

class College:
def **init**(self, student):
self.student = student

student = Student("Piyush")
college = College(student)

The student can exist even if the College object is destroyed.

Interview Answer:
"Aggregation is a weak has-a relationship in which the child object can exist independently of the parent object."

Example:
College HAS-A Student
'''

# Composition

'''
Composition is a strong "has-a" relationship.

The contained object is strongly associated with the owner and is normally created as part of the owner.

Example:
class Engine:
def start(self):
print("Engine started")

class Car:
def **init**(self):
self.engine = Engine()

```
def start(self):
    self.engine.start()
```

car = Car()
car.start()

The Car creates and owns its Engine.

Interview Answer:
"Composition is a strong has-a relationship where the contained object's lifecycle is closely tied to the owner."

Example:
Car HAS-A Engine

If the Car is removed, its Engine is also considered part of that Car and does not have an independent relationship with another Car.
'''

# ⭐ Most Important Interview Differences

'''
Class vs Object:
Class = Blueprint
Object = Instance of a class

Encapsulation vs Abstraction:
Encapsulation = Protect/bundle data and methods
Abstraction = Hide implementation details

Inheritance vs Composition:
Inheritance = IS-A relationship
Composition = HAS-A relationship

Overloading vs Overriding:
Overloading = Same method name with different parameters
Overriding = Child class changes parent's method implementation

Aggregation vs Composition:
Aggregation = Weak HAS-A relationship; objects can exist independently
Composition = Strong HAS-A relationship; lifecycle is closely connected

Class Variable vs Instance Variable:
Class variable = Shared by all objects
Instance variable = Separate for each object
'''

# ⭐ One-Line Interview Revision

'''
OOP:
Programming using classes and objects.

Class:
Blueprint for creating objects.

Object:
Instance of a class.

Constructor:
**init**() initializes an object.

Encapsulation:
Wrapping data and methods together and controlling access.

Inheritance:
Child class acquires properties and methods of parent class.

Polymorphism:
Same interface/method can have different behavior.

Abstraction:
Hiding implementation details and showing essential functionality.

Overloading:
Same method name with different parameter patterns; Python does not support traditional overloading.

Overriding:
Child class provides its own implementation of a parent method.

Public:
Accessible normally.

Protected:
Single underscore _; convention for internal use.

Private:
Double underscore __; name mangling is applied.

Class Variable:
Shared among objects.

Instance Variable:
Specific to an object.

Association:
General relationship between independent objects.

Aggregation:
Weak HAS-A relationship.

Composition:
Strong HAS-A relationship.
'''


'''
---------------------------------------------1. SOLID Principles in Python

SOLID is a set of 5 principles used to write code that is clean, maintainable, reusable, and easy to extend.

The five principles are:

Letter	Principle	Simple meaning
S	Single Responsibility Principle	One class → one responsibility
O	Open/Closed Principle	Extend code without modifying existing code
L	Liskov Substitution Principle	Child class should properly replace parent class
I	Interface Segregation Principle	Don't force classes to implement unnecessary methods
D	Dependency Inversion Principle	Depend on abstractions, not concrete classes


S — Single Responsibility Principle (SRP)
Concept

A class should have only one responsibility or one main reason to change.

❌ Bad example
class Employee:
    def calculate_salary(self):
        pass

    def save_to_database(self):
        pass

    def generate_report(self):
        pass

This class is doing three different jobs:

Salary calculation
Database operations
Report generation

If the database logic changes, we have to modify Employee.

✅ Better example

Separate responsibilities:

class SalaryCalculator:
    def calculate_salary(self, employee):
        return employee.salary


class EmployeeRepository:
    def save(self, employee):
        print("Saving employee to database")


class ReportGenerator:
    def generate(self, employee):
        print("Generating employee report")

Now each class has a clear responsibility.

Interview answer

SRP means a class should have one responsibility and one reason to change.

O — Open/Closed Principle (OCP)
Concept

Software should be:

Open for extension, but closed for modification.

This means we should be able to add new functionality without changing existing working code.

❌ Bad example
class Payment:
    def pay(self, payment_type):
        if payment_type == "card":
            print("Paying using card")
        elif payment_type == "upi":
            print("Paying using UPI")
        elif payment_type == "cash":
            print("Paying using cash")

Suppose tomorrow we add:

PayPal
Google Pay
Apple Pay

We have to keep modifying the existing class.

✅ Better example

Use polymorphism:

class Payment:
    def pay(self):
        pass


class CardPayment(Payment):
    def pay(self):
        print("Paying using card")


class UPIPayment(Payment):
    def pay(self):
        print("Paying using UPI")


class CashPayment(Payment):
    def pay(self):
        print("Paying using cash")

Now:

payments = [
    CardPayment(),
    UPIPayment(),
    CashPayment()
]

for payment in payments:
    payment.pay()

If we want PayPal:

class PayPalPayment(Payment):
    def pay(self):
        print("Paying using PayPal")

We extend the system without modifying the existing payment classes.

Interview answer

OCP means existing code should be closed for modification but open for adding new functionality through extension.

L — Liskov Substitution Principle (LSP)
Concept

A child class should be able to replace its parent class without breaking the program.

In simple words:

If B is a subclass of A, wherever we expect A, we should be able to use B.

Example
class Bird:
    def fly(self):
        print("Flying")


class Sparrow(Bird):
    def fly(self):
        print("Sparrow flying")

This works because a sparrow can fly.

But consider:

class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins cannot fly")

Now:

def make_bird_fly(bird):
    bird.fly()


make_bird_fly(Penguin())

The program breaks.

So Penguin should not inherit from a parent that promises that every bird can fly.

✅ Better design
class Bird:
    def eat(self):
        print("Eating")


class FlyingBird(Bird):
    def fly(self):
        print("Flying")


class Sparrow(FlyingBird):
    pass


class Penguin(Bird):
    pass

Now the hierarchy makes more sense.

Interview answer

LSP says that derived classes must be substitutable for their base classes without changing the correctness of the program.

I — Interface Segregation Principle (ISP)

Python doesn't have interfaces in exactly the same way as Java, but we can demonstrate the principle using abstract base classes.

Concept

A class should not be forced to implement methods it doesn't need.

❌ Bad example
from abc import ABC, abstractmethod


class Worker(ABC):

    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass

Now imagine a robot:

class Robot(Worker):

    def work(self):
        print("Robot working")

    def eat(self):
        raise Exception("Robot doesn't eat")

The robot is being forced to implement eat() even though it doesn't need it.

✅ Better

Split the interface:

from abc import ABC, abstractmethod


class Workable(ABC):

    @abstractmethod
    def work(self):
        pass


class Eatable(ABC):

    @abstractmethod
    def eat(self):
        pass

Human:

class Human(Workable, Eatable):

    def work(self):
        print("Human working")

    def eat(self):
        print("Human eating")

Robot:

class Robot(Workable):

    def work(self):
        print("Robot working")

The robot only implements what it needs.

Interview answer

ISP says that clients should not be forced to depend on methods they don't use. Prefer small, specific interfaces over large interfaces.

D — Dependency Inversion Principle (DIP)
Concept

High-level classes should not directly depend on low-level classes.

Instead:

Both should depend on abstractions.

❌ Bad example
class MySQLDatabase:

    def save(self, data):
        print("Saving to MySQL")


class UserService:

    def __init__(self):
        self.database = MySQLDatabase()

    def save_user(self, user):
        self.database.save(user)

UserService is tightly coupled to MySQLDatabase.

If we want MongoDB, we need to change UserService.

✅ Better

Create an abstraction:

from abc import ABC, abstractmethod


class Database(ABC):

    @abstractmethod
    def save(self, data):
        pass

MySQL:

class MySQLDatabase(Database):

    def save(self, data):
        print("Saving to MySQL")

MongoDB:

class MongoDB(Database):

    def save(self, data):
        print("Saving to MongoDB")

Now UserService depends on the abstraction:

class UserService:

    def __init__(self, database):
        self.database = database

    def save_user(self, user):
        self.database.save(user)

We can use either:

mysql = MySQLDatabase()
service = UserService(mysql)

service.save_user("Piyush")

or:

mongo = MongoDB()
service = UserService(mongo)

service.save_user("Piyush")

No change to UserService.

Interview answer

DIP says high-level modules should depend on abstractions rather than concrete implementations.

SOLID — Quick Revision

Remember this:

S → Single responsibility
    One class = one main job

O → Open/Closed
    Add functionality without modifying existing code

L → Liskov substitution
    Child should safely replace parent

I → Interface segregation
    Don't force unnecessary methods

D → Dependency inversion
    Depend on abstractions, not concrete classes
Easy real-world example

Imagine you're building an online car rental system:

S → Booking handles booking
    Payment handles payment
    Notification handles notifications

O → Add UPI payment without rewriting existing payment logic

L → Different vehicle types should behave correctly wherever
    the base vehicle type is expected

I → Don't force a car class to implement bike-specific operations

D → BookingService depends on a Payment interface,
    not directly on Razorpay/Stripe/etc.
'''