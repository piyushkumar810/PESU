# -------------------------------
# Composition in Python Example
# -------------------------------
# Composition means "HAS-A" relationship.
# A Laptop HAS-A Processor, HAS-A Battery, HAS-A Screen, HAS-A Keyboard.
# Instead of inheriting, we combine smaller classes into a bigger one.

# Component class: Processor
class Processor:
    def _init_(self, brand, cores):
        self.brand = brand
        self.cores = cores

    def process(self):
        print(f"Processor running with {self.cores} cores ({self.brand})")

# Component class: Battery
class Battery:
    def _init_(self, capacity):
        self.capacity = capacity  # in mAh

    def charge(self):
        print(f"Battery charging ... Capacity: {self.capacity}mAh")

    def discharge(self):
        print("Battery discharging ...")

# Component class: Screen
class Screen:
    def _init_(self, size):
        self.size = size  # in inches

    def display(self, content):
        print(f"Displaying on {self.size}-inch screen: {content}")

# Component class: Keyboard
class Keyboard:
    def _init(self, type):
        self.type = type

    def type_key(self, key):
        print(f"Key '{key}' pressed on {self.type} keyboard")

# Composite class: Laptop (HAS-A relationship with Processor, Battery, Screen, Keyboard)
class Laptop:
    def _init_(self, brand, model):
        self.brand = brand
        self.model = model

        # Composition: creating objects of other classes inside Laptop
        self.processor = Processor("Intel i7", 8)
        self.battery = Battery(6000)
        self.screen = Screen(15.6)
        self.keyboard = Keyboard("Backlit")

    def power_on(self):
        print(f"{self.brand} {self.model} powering ON ...")
        self.processor.process()   # Delegating work to Processor object

    def show_display(self, message):
        self.screen.display(message)  # Delegating work to Screen object

    def charge_laptop(self):
        self.battery.charge()  # Delegating work to Battery object

    def use_keyboard(self, key):
        self.keyboard.type_key(key)  # Delegating work to Keyboard object

# -------------------------------
# Object Creation and Usage
# -------------------------------
my_laptop = Laptop("Dell", "XPS 15")

# Using composed objects through Laptop
my_laptop.power_on()
my_laptop.show_display("Welcome to your system!")
my_laptop.use_keyboard("Enter")
my_laptop.charge_laptop()


print(type(Processor))
