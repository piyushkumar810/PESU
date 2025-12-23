'''
📘 Problem Statement 9: E-Commerce Returns - Excel to CSV with Error Log
Question

Write a Python program to process e-commerce return requests using an Excel file.

An Excel file named returns.xlsx is provided with the following columns:
ReturnID, OrderID, Reason, Amount, RefundMode.

The program should perform the following tasks:
    Read the Excel file from disk.
    Validate each row based on the following rules:
    RefundMode must be one of: UPI, CARD, or WALLET.
    Amount must be greater than 0.

Write all valid rows to a CSV file named returns_clean.csv.

Write all invalid rows to an Excel file named returns_error_log.xlsx,
'''