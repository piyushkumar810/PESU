# when one class inherits from another, it automatically takes on all the attributes and method of the first class

# advantage
# reusability of code

class Laptop:
    """Represent a general laptop."""
    def __init__(self, brand, model, price):
        """Initialize attributes of a general laptop."""
        self.brand = brand
        self.model = model
        self.price = price

    def show_details(self):
        """Display laptop details."""
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: ₹{self.price}")

    def turn_on(self):
        print(f"{self.brand} {self.model} is now ON.")

    def turn_off(self):
        print(f"{self.brand} {self.model} is now OFF.")
        

class GamingLaptop(Laptop):
    """Represent aspects of a laptop specific to a gaming laptop."""
    def __init__(self, brand, model, price, gpu):
        """Initialize attributes of the parent class and add gaming-specific ones."""
        super().__init__(brand, model, price)
        self.gpu = gpu

    def boot_mode(self):
        """Simulate enabling gaming boot mode."""
        print(f"{self.brand} {self.model} is running in gaming boot mode with {self.gpu} GPU!")


# Example usage
gl1 = GamingLaptop("Asus", "ROG Strix G15", 145000, "NVIDIA RTX 4070")
gl1.show_details()
gl1.boot_mode()
