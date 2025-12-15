
class Booking:
    def __init__(self, booking_id, user, car, days):
        self.booking_id = booking_id
        self.user = user
        self.car = car
        self.days = days
        self.total_amount = car.price_per_day * days
