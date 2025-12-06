# Create three classes: Device (base) with device_name Laptop (inherits from Device)
#  with processor GamingLaptop (inherits from Laptop) with gpu Display full configuration 
#  using a method in the derived class.

class Device:
    def __init__(self, device_name):
        self.device_name = device_name

    def show_device(self):
        print("Device Name:", self.device_name)


class Laptop(Device):
    def __init__(self, device_name, processor):
        super().__init__(device_name)
        self.processor = processor

    def show_laptop(self):
        self.show_device()
        print("Processor:", self.processor)


class GamingLaptop(Laptop):
    def __init__(self, device_name, processor, gpu):
        super().__init__(device_name, processor)
        self.gpu = gpu

    def show_full_config(self):
        self.show_laptop()
        print("GPU:", self.gpu)


gl = GamingLaptop("ASUS ROG", "Intel i9", "NVIDIA RTX 4070")
gl.show_full_config()
