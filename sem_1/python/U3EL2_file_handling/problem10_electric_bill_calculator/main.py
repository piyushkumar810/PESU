'''
📘 Problem Statement 10: Electricity Bill Calculator – CSV to Excel Bills
Question

Write a Python program to calculate electricity bills using a CSV file.

A CSV file named meter_readings.csv is provided with the following columns:
ConsumerID, Name, PreviousReading, CurrentReading.

The program should perform the following tasks:
    Read the CSV file from disk.
    Compute Units Consumed as:
        Units = CurrentReading - PreviousReading.
    If the calculated Units is negative, mark the row as invalid.
    Apply the following billing slabs:
        First 100 units → ₹4 per unit
        Next 100 units → ₹6 per unit
        Above 200 units → ₹8 per unit

    Create an Excel file named bills.xlsx with the columns:
        ConsumerID
        Name
        Units
        BillAmount

    Write all invalid rows to a CSV file named billing_errors.csv with an additional column ErrorReason.
'''
