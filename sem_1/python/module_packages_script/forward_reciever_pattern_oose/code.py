class Car:              # Receiver
    def reserve(self):
        return "Car reserved"


class BookingDispatcher:  # Forwarder
    def __init__(self):
        self.car = Car()

    def send(self):
        return self.car.reserve()


class Customer:          # Initiator
    def ask(self, dispatcher):
        print(dispatcher.send())


d = BookingDispatcher()
c = Customer()
c.ask(d)
