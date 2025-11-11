class cat:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def info(self):
        print(f"i am a cat. my name is {self.name}, i am {self.age} year old. ")

    def make_sound(slef):
        print("MEOW")

class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        print(f"i am a dog. my name is {self.name}, i am {self.age} year old. ")

    def make_sound(slef):
        print("Bark")

cat1=cat("kitty", 2)
dog1=dog("Bruno", 3)

cat1.info()
dog1.info()

for animal in (cat1,dog1):
    animal.info()
    animal.make_sound()

cat1.make_sound()
dog1.make_sound()

# ---------------------------------------- duck typing---------------------------

class duck:
    def quack(self):
        print("i am a duck and i quack.")

class goose:
    def quack(self):
        print("i am a goose and a quack")

class cat:
    def meow(self):
        print("i am a cat and i meow")

def quack(animal):
    animal.quack()

duck1 = duck()
goose1 = goose()
cat1 = cat()
