# A student class stores the academic year for all students. A class method is used to change the year during promotion.
#  You are asked to update the year and validate the change using sample objects.

class Students:
    academic_year = "1st Year"
    
    def __init__(self, name):
        self.name = name
        
    @classmethod
    def promote_year(cls, new_year):
        cls.academic_year = new_year
        
    def show(self):
        print(self.name, "", Students.academic_year)
            
            
s1 = Students("Piyush")
s2 = Students("Praneeth")

print("Before Promotion:")
s1.show()
s2.show()

Students.promote_year("2nd Year")

print("\nAfter Promotion:")
s1.show()
s2.show()
