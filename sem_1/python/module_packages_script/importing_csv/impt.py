import csv
with open("C://Users//piyush kumar//Downloads//data.csv","r") as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)

# this is wrong()
import csv
with open("C://Users//piyush kumar//Downloads//data1.csv","r") as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)

print("_"*20)


# correct reading(specifying delimiter)
import csv
with open("C://Users//piyush kumar//Downloads//data1.csv","r") as file:
    reader=csv.reader(file,delimiter=";")
    for row in reader:
        print(row)


import csv
with open("C://Users//piyush kumar//Downloads//data_2.csv","r") as file:
    fildname=["Nam","Age","Profession"]
    reader=csv.DictReader(file,fieldnames=fildname)
    for row in reader:
        print(row)
