# class , object and constructor
class praneeth:
    def __init__(self,name,srn):
        self.name=name
        self.srn=srn

    def personal_info(self):
        print(self.name +" roll no is "+ self.srn)


pray=praneeth("praneeth" , "pesu1pg25ca169")
pray.personal_info()

pray2=praneeth("piyush","orjgoerg")

# print(pray2.name)
pray2.personal_info()

