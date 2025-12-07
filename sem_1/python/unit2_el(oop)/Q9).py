# A membership class keeps a standard discount for all members. A class method is used 
# to revise this discount. You are asked to apply the new discount and show its impact 
# on two purchases.

class Membership:
    discount = 10

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def update_discount(cls, new_discount):
        cls.discount = new_discount

    def final_price(self):
        return self.price - (self.price * Membership.discount / 100)


p1 = Membership("Purchase 1", 1000)
p2 = Membership("Purchase 2", 2000)

print("Before Discount Change:")
print(p1.name, "→", p1.final_price())
print(p2.name, "→", p2.final_price())

Membership.update_discount(20)

print("\nAfter Discount Change:")
print(p1.name, "→", p1.final_price())
print(p2.name, "→", p2.final_price())
