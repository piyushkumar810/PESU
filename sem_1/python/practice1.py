# multilevel_inheritance

class employee:
    def __init__(self,name):
        self.name=name

    def show(self):
        print("the name of employee is : ", self.name)

class dancer:
    def __init__(self,dance):
        self.dance=dance

    def show(self):
        print(f"the dance is {self.dance}")

class DancerEmployee(employee,dancer):
    def __init__(self,dance, name):
        self.dance=dance
        self.name=name

o=DancerEmployee("kathak","shivani")
print(o.name)
print(o.dance)

o.show()