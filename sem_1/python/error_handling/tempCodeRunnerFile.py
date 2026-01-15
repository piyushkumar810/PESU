class AgeError(Exception):
    pass

try:
    age = 15
    if age < 18:
        raise AgeError("Age must be greater than 18")
except AgeError:
    print("Not eligible")
