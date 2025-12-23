# question
'''
📘 Question

Write a Python program to analyze student attendance using an Excel file.

An Excel file named attendance.xlsx contains a sheet named Sheet1 with the following columns:
StudentID, Name, DaysPresent, TotalDays.

The program should perform the following tasks:
    Read the Excel file using a Python library.
    Calculate the attendance percentage for each student.
    Add a new column named AttendanceStatus.
    Set the status as "Shortage" if the attendance percentage is below 75.
    Save the updated data into a new Excel file named attendance_report.xlsx.
'''

import pandas as pd

# Create the data
data = {
    "StudentID": [101, 102, 103, 104],
    "Name": ["Piyush", "Rohit", "Aman", "Neha"],
    "DaysPresent": [65, 80, 60, 85],
    "TotalDays": [90, 90, 90, 90]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to Excel
df.to_excel(
    "C://Users//piyush kumar//OneDrive//Desktop//GitHub//PESU//sem_1//python//U3EL2_file_handling//problem3_attendence//attendance.xlsx",
    index=False
)
print("attendance.xlsx file created successfully.")

# Read Excel file
df = pd.read_excel(
    "C://Users//piyush kumar//OneDrive//Desktop//GitHub//PESU//sem_1//python//U3EL2_file_handling//problem3_attendence//attendance.xlsx",
    sheet_name="Sheet1"
)

# Calculate attendance percentage
df["AttendancePercentage"] = (df["DaysPresent"] / df["TotalDays"]) * 100

# Add attendance status
df["AttendanceStatus"] = df["AttendancePercentage"].apply(
    lambda x: "Shortage" if x < 75 else "OK"
)

# Save updated report
df.to_excel(
    "C://Users//piyush kumar//OneDrive//Desktop//GitHub//PESU//sem_1//python//U3EL2_file_handling//problem3_attendence//attendance_report.xlsx",
    index=False
)

print("attendance_report.xlsx created successfully.")
