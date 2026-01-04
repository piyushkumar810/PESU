# ---------------- SERVER ----------------
class Car:
    def reserve(self):
        return "Car reserved successfully"


# ---------------- DISPATCHER ----------------
class BookingDispatcher:
    def __init__(self):
        # service registry (name → server object)
        self.services = {}

    def register_service(self, name, service):
        self.services[name] = service

    def get_service(self, name):
        if name in self.services:
            return self.services[name]
        else:
            raise Exception("Requested service not available")


# ---------------- CLIENT ----------------
class Customer:
    def book_car(self, dispatcher):
        try:
            # ask dispatcher for service
            car_service = dispatcher.get_service("CarService")
            # use service
            result = car_service.reserve()
            print(result)
        except Exception as e:
            print(e)


# ---------------- MAIN ----------------
dispatcher = BookingDispatcher()

# server registers itself
car = Car()
dispatcher.register_service("CarService", car)

# client requests service
customer = Customer()
customer.book_car(dispatcher)
'''
One-line definition:
-> The Client does not directly talk to the Server.
-> A Dispatcher sits in between and locates + provides the requested service.

| Role                          | Class               | Responsibility               |
| ----------------------------- | ------------------- | ---------------------------- |
| **Server / Service Provider** | `Car`               | Provides actual service      |
| **Dispatcher / Broker**       | `BookingDispatcher` | Registers & locates services |
| **Client**                    | `Customer`          | Requests service             |
| **Service Registry**          | `services` dict     | Stores services              |
'''