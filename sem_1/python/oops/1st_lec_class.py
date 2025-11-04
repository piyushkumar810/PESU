class student:
    def __init__(self,name,course):
        self.name=name
        self.course=course

    def inntroduce(self):
        print("hello, my name is", self.name)
        print("i am studing", self.course)


s1=student("xyz", "programming with python")
s1.inntroduce()