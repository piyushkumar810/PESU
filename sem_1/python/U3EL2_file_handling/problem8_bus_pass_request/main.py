'''
📘 Problem Statement 8: Bus Pass Requests - CSV to Excel with Status Tracking
Question

Write a Python program to process bus pass requests using a CSV file and generate outputs in Excel and CSV formats.

A CSV file named bus_pass_requests.csv is provided with the following columns:
ReqID, StudentID, Route, DistanceKm, RequestedOn.

The program should perform the following tasks:
    Read the CSV file from disk.
    Compute the Fare based on distance slabs:
        0 to 5 km → Fare = 400
        6 to 10 km → Fare = 650
        Above 10 km → Fare = 900

    Create an Excel file named bus_pass_status.xlsx.
    Add a new column Status.
        Set Status = "Pending" for all rows.

    Create a separate CSV file named bus_pass_fare_list.csv containing only:
        ReqID
        StudentID
        Fare
'''

import pandas as pd

df=pd.read_csv("C://Users//piyush kumar//OneDrive//Desktop//GitHub//PESU//sem_1//python//U3EL2_file_handling//problem8_bus_pass_request//bus_pass_requests.csv")
print(df.to_string(index=False))

# Step 2: Function to calculate fare using slabs
def calculate_fare(distance):
    if distance <= 5:
        return 400
    elif distance <= 10:
        return 650
    else:
        return 900

# Step 3: Calculate Fare column
df["Fare"] = df["DistanceKm"].apply(calculate_fare)

# Step 4: Add Status column with "Pending"
df["Status"] = "Pending"

# Step 5: Save full data with status to Excel
df.to_excel("bus_pass_status.xlsx", index=False)

# Step 6: Create separate CSV with required columns
fare_df = df[["ReqID", "StudentID", "Fare"]]
fare_df.to_csv("C://Users//piyush kumar//OneDrive//Desktop//GitHub//PESU//sem_1//python//U3EL2_file_handling//problem8_bus_pass_request//bus_pass_fare_list.csv", index=False)

print("bus_pass_status.xlsx and bus_pass_fare_list.csv created successfully.")