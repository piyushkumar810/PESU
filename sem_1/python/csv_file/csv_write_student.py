# import csv

# with open("C:\\Users\\piyush kumar\\OneDrive\\Desktop\\GitHub\\PESU\\sem_1\\python\\csv_file\\students.csv", "w", newline="", encoding="utf-8") as file:
#     writer = csv.writer(file)

#     # Header row
#     writer.writerow(["Name", "Age", "Course"])

#     # Data rows
#     writer.writerow(["Piyush", 21, "Python"])
#     writer.writerow(["Amit", 22, "Java"])
#     writer.writerow(["Riya", 20, "C++"])

# print("CSV file written successfully")


# -----------------------------  writing in dictionary
import csv

with open("C:\\Users\\piyush kumar\\OneDrive\\Desktop\\GitHub\\PESU\\sem_1\\python\\csv_file\\employees.csv", "w", newline="", encoding="utf-8") as file:
    fieldnames = ["name", "department", "salary"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    # Write header
    writer.writeheader()

    # Write rows
    writer.writerow({"name": "Jack", "department": "HR", "salary": 50000})
    writer.writerow({"name": "Jill", "department": "IT", "salary": 60000})
    writer.writerow({"name": "Peter", "department": "Finance", "salary": 55000})

print("employees.csv created")
