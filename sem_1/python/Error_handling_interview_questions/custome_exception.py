class SalaryNotInRangeError(Exception):
    """Exception raised when salary is outside the valid range."""

    def __init__(self, salary, message="Salary is not in (5000, 15000) range"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)


try:
    salary = int(input("Enter salary amount: "))

    if not 5000 < salary < 15000:
        raise SalaryNotInRangeError(salary)

except SalaryNotInRangeError as e:
    print("Custom Exception Caught!")
    print("Message:", e)
    print("Invalid Salary:", e.salary)

except ValueError:
    print("Invalid input! Please enter a number.")

else:
    print("Salary accepted:", salary)

finally:
    print("Program execution completed.")
