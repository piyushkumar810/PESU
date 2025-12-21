# -------- Subscriber Interface --------
class Subscriber:
    def update(self, message):
        pass


# -------- Concrete Subscriber 1 --------
class CustomerNotification(Subscriber):
    def update(self, message):
        print("Customer Notification:", message)


# -------- Concrete Subscriber 2 --------
class AdminNotification(Subscriber):
    def update(self, message):
        print("Admin Notification:", message)


# -------- Publisher --------
class BookingService:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self.subscribers.remove(subscriber)

    def notify(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)

    def confirm_booking(self):
        print("Booking confirmed")
        self.notify("Your car booking is confirmed")


# -------- Main Flow --------
booking_service = BookingService()

customer = CustomerNotification()
admin = AdminNotification()

booking_service.subscribe(customer)
booking_service.subscribe(admin)

booking_service.confirm_booking()
