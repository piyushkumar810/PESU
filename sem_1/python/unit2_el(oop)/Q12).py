# A temperature class uses a class method to convert Fahrenheit to Celsius. 
# You must create an instance through this method and print the converted value.

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @classmethod
    def from_fahrenheit(cls, f):
        c = (f - 32) * 5/9        # convert F → C
        return cls(c)             # create object using Celsius value

# Create object using class method
temp = Temperature.from_fahrenheit(98.6)

# Print the converted Celsius value
print("Temperature in Celsius:", temp.celsius)
