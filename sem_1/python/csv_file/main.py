# import csv

# with open("C:\\Users\\piyush kumar\\OneDrive\\Desktop\\GitHub\\PESU\\sem_1\\python\\csv_file\\file.csv", "r", encoding="utf-8") as file:
#     reader = csv.reader(file,skipinitialspace=True)
#     # print(reader)
#     print(type(reader))
    
#     for row in reader:
#         print(row)


import csv

with open("C:\\Users\\piyush kumar\\OneDrive\\Desktop\\GitHub\\PESU\\sem_1\\python\\csv_file\\file.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=";",skipinitialspace=True)

    for row in reader:
        print(row)


#------------------- csv dictReader
import csv

with open("C:\\Users\\piyush kumar\\OneDrive\\Desktop\\GitHub\\PESU\\sem_1\\python\\csv_file\\file.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file, fieldnames=["name","age","job"])

    for row in reader:
        print(row)


