# Create a base class Transport and subclasses Car, Bike, and Bus, each with a method capacity() 
# returning passenger limits. Use polymorphism to display capacity for all subclasses in a loop.

class Transport:
    def capacity(self):
        return "Unknown capacity"


class Car(Transport):
    def capacity(self):
        return "Car can carry 4 passengers"


class Bike(Transport):
    def capacity(self):
        return "Bike can carry 2 passengers"


class Bus(Transport):
    def capacity(self):
        return "Bus can carry 50 passengers"


vehicles = [Car(), Bike(), Bus()]

for v in vehicles:
    print(v.capacity())
