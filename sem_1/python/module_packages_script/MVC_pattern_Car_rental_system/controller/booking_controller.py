from model.booking import Booking

class BookingController:
    def __init__(self, cars):
        self.cars = cars
        self.booking_counter = 1

    def book_car(self, user, car_id, days):
        for car in self.cars:
            if car.car_id == car_id and car.available:
                car.mark_unavailable()
                booking = Booking(self.booking_counter, user, car, days)
                self.booking_counter += 1
                return booking
        return None
