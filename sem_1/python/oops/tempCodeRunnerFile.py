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