class Car:
    def __init__(self, car_id, model, price_per_day, available=True):
        self.car_id = car_id
        self.model = model
        self.price_per_day = price_per_day
        self.available = available

    def mark_unavailable(self):
        self.available = False

    def mark_available(self):
        self.available = True
