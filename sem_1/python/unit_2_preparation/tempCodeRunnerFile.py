class prot:
    def __init__(self):
        self.__n=405
    
    def diplay(self):
        print(f"my value is private {self.__n}")

prot1=prot()
prot1.diplay()
print(prot1.__n)