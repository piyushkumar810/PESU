
# incorrect
import csv
with open("C://Users//piyush kumar//Downloads//data1.csv","r") as file:
    csv_reader=csv.DictReader(file)
    for row in csv_reader:
        print(row)

print("_"*20)


# correct way
import csv
with open("C://Users//piyush kumar//Downloads//data1.csv","r") as file:
    csv_reader=csv.DictReader(file,delimiter=";")
    for row in csv_reader:
        print(row)
