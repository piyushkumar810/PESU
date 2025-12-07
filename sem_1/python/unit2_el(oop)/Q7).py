# Base class Employee with name, ID, and base salary. Derived classes FullTimeEmployee (adds bonus) 
# and PartTimeEmployee (adds hourly rate and hours). A method calculate_pay() overridden in each subclass. 
# Print the pay details for each employee type using a polymorphic list.

# class employee:
#     def __init__(self,name,id,base_salary):
#         self.name=name
#         self.id=id
#         self.base_salary=base_salary

    
# class full_time_employee(employee):
#     def __init__(self,name,id,base_salary,bonus):
#         super.__init__(name,id,base_salary)
#         self.bonus=bonus

#     def calculate_pay(self):
#         pay_total=self.base_salary+self.bonus
#         print("Employee Name = ",self.name)
#         print("Employee id = ",self.id)
#         print("His total income is = ",pay_total)

# class part_time_employee(employee):
#     def __init__(self,name,id,base_salary,bonus,hourly_rate,hours):
#         super.__init__(name,id,base_salary,bonus)
#         self.hourly_rate=hourly_rate
#         self.hours=hours

#     def calculate_pay(self):
#         hourly_total=self.hourly_rate*self.hours

#         pay_total=self.base_salary+self.bonus
#         print("Employee Name = ",self.name)
#         print("Employee id = ",self.id)
#         print("His total income is = ",pay_total)

# -----------------------------------------------------------------------------------------
class Employee:
    def __init__(self, name, emp_id, base_salary):
        self.name = name
        self.emp_id = emp_id
        self.base_salary = base_salary

    def calculate_pay(self):
        return self.base_salary


class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, base_salary, bonus):
        super().__init__(name, emp_id, base_salary)
        self.bonus = bonus

    def calculate_pay(self):
        return self.base_salary + self.bonus


class PartTimeEmployee(Employee):
    def __init__(self, name, emp_id, base_salary, hourly_rate, hours):
        super().__init__(name, emp_id, base_salary)
        self.hourly_rate = hourly_rate
        self.hours = hours

    def calculate_pay(self):
        return self.base_salary + (self.hourly_rate * self.hours)


e1 = FullTimeEmployee("Amit", 101, 20000, 5000)
e2 = PartTimeEmployee("Riya", 102, 5000, 300, 40)

employees = [e1, e2]

for emp in employees:
    print(emp.name, "→ Pay:", emp.calculate_pay())
