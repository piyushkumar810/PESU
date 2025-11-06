'''
🧩 What is __init__?

__init__ is a special method (also called a constructor) in Python classes.
It automatically runs when you create (initialize) a new object from a class.
It is used to assign initial values to the object’s attributes.
'''

# self--> refers to the current object


class laptop:
    def __init__(self, brand, model,price):
        self.brand=brand
        self.model=model
        self.price=price

    def turn_on(self):
        print(f"{self.brand} {self.model} is now ON")

    def turn_off(self):
        print(f"{self.brand} {self.model} is now OFF")

    def brand_price(self):
        print(f"{self.brand} {self.model} {self.price}is now ON")

l1=laptop("DEll", "inspiron 15", 55000)
l2=laptop("Apple", "macbook air", 120000)
l1.turn_on()
l1.turn_off()
l1.brand_price()


# Q2) create a class car with two attributes (brand and model) also add a method display_info() to print the detail

class car:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model

    def display_info(self):
        print(f"my car brand is {self.brand} and model is {self.model}")

car1=car("maruti", "xuv700")
car1.display_info()

# Q3) create a siimple calculator wwhich takes two parameter perform method (add, sub, multiply, divide)

class calculator:
    def __init__(self, a,b):
        self.a=a
        self.b=b

    def add(self):
        print(f"addition of these two value = {self.a+self.b}")

    def sub(self):
        print(f"substraction of these two value = {self.a-self.b}")

    def mul(self):
        print(f"multiplicatino of these two value = {self.a*self.b}")

    def division(self):
        print(f"division of these two value is {self.a/self.b}")

cal=calculator(50,5)
cal.add()
cal.sub()
cal.mul()
cal.division()
