# peer-to-peer communication

'''
-> Roles in Your Code (VERY IMPORTANT)
Role	Class	Responsibility
Initiator	Customer	Starts the request
Forwarder	BookingDispatcher	Forwards request
Receiver	Car	  Does the actual work
'''
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
# One object (Forwarder) receives a request and forwards it to another object (Receiver) that actually does the work.
# Why do we use it?

# To decouple (separate) the requester from the actual worker
# The requester does not know who really performs the operation
# Makes systems flexible, maintainable, and extensible