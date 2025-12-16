import csv
with open("C://Users//piyush kumar//Downloads//data1.csv","r") as file:
    csv_reader=csv.DictReader(file,delimiter=";")
    for row in csv_reader:
        print(row)
