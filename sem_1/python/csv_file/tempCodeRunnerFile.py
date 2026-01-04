import csv

with open("C:\\Users\\piyush kumar\\OneDrive\\Desktop\\GitHub\\PESU\\sem_1\\python\\csv_file\\file.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file, fieldnames=["name","age","job"])

    for row in reader:
        print(row)