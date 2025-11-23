class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    pass

class Developer(Employee):
    pass

class Tester(Employee):
    pass

m = Manager("Rohan", 55000)
d = Developer("Piyush", 70000)
t = Tester("Aman", 45000)

employees = [m, d, t]

highest = max(employees, key=lambda x: x.salary)

print("Highest Salary:", highest.name, highest.salary)
