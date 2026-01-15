class SalaryNotInRangeErrror(Exception):
    def __init__(self,salary,message="salary should be in the rnage of (5000 ,15000) range"):
        self.salary=salary
        self.message=message
        super().__init__(self.message)

salary=int(input("enter a salary"))
if not 5000<salary<15000:
    raise SalaryNotInRangeErrror(salary)