class Driver:
    def work(self, msg):
        return "Ride confirmed: " + msg


class TaxiDispatcher:
    def _init_(self):
        self.driver = Driver()

    def send(self, msg):
        print("Dispatcher got the request")
        return self.driver.work(msg)


class Customer:
    def ask(self, dispatcher, msg):
        print("Customer sending request")
        result = dispatcher.send(msg)
        print("Customer got reply:", result)


d = TaxiDispatcher()
c = Customer()

c.ask(d, "Driver details")