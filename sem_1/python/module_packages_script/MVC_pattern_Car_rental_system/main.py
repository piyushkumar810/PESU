from model.car import Car
from model.user import User
from view.user_view import UserView
from controller.booking_controller import BookingController

# Sample Data
cars = [
    Car(1, "Swift", 1500),
    Car(2, "Creta", 3000),
    Car(3, "Innova", 3500)
]

user = User(101, "Piyush", "DL12345")

# MVC Wiring
view = UserView()
controller = BookingController(cars)

# Flow
view.show_available_cars(cars)
booking = controller.book_car(user, 2, 3)

if booking:
    view.show_booking_confirmation(booking)
else:
    print("Car not available")
