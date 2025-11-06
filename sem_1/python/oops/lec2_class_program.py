class Laptop:
    def __init__(self, brand, battery_level=100):
        self.brand = brand
        self.battery_level = battery_level

    def update_battery_level(self, new_level):
        """Set the battery level to the given value."""
        if 0 <= new_level <= 100:
            self.battery_level = new_level
            print(f"Battery level updated to {self.battery_level}%.")
        else:
            print("Invalid battery level! Please enter a value between 0 and 100.")

    def decrease_battery(self, amount):
        """Decrease battery by given amount."""
        if amount < 0:
            print("Invalid amount! It must be positive.")
        elif self.battery_level - amount < 0:
            self.battery_level = 0
            print("Battery completely drained!")
        else:
            self.battery_level -= amount
            print(f"Battery decreased by {amount}%. Current level: {self.battery_level}%.")

    def check_battery(self):
        """Display current battery level."""
        print(f"Current battery level: {self.battery_level}%.")


# Create object
laptop1 = Laptop("Dell")

# Test the functions
laptop1.update_battery_level(90)
laptop1.decrease_battery(15)
laptop1.decrease_battery(50)
laptop1.check_battery()
