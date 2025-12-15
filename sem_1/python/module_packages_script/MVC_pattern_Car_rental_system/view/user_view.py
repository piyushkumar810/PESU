
class UserView:
    def show_available_cars(self, cars):
        print("\nAvailable Cars:")
        for car in cars:
            if car.available:
                print(f"{car.car_id} - {car.model} - ₹{car.price_per_day}/day")

    def show_booking_confirmation(self, booking):
        print("\nBooking Confirmed!")
        print(f"Booking ID: {booking.booking_id}")
        print(f"Car: {booking.car.model}")
        print(f"Total Amount: ₹{booking.total_amount}")
