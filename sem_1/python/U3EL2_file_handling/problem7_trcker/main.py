# 📘 Problem Statement 7: Monthly Expense Tracker Using Excel
'''
Question
Write a Python program to track monthly expenses using an Excel file.

An Excel file named expenses.xlsx contains daily expense details with the following columns:
Date, Category, Amount.

The program should perform the following tasks:
    Read the Excel file completely from disk.
    Calculate the monthly total expense for each Category.
    Create a new Excel file named monthly_summary.xlsx.
    Write each Category along with its total expense into the new file.
'''
import pandas as pd
df=pd.read_excel("C://Users//piyush kumar//Downloads//expenses.xlsx")

print("Original Expense Data:")
print(df.to_string(index=False))

# Step 2: Group data by Category
grouped_data = df.groupby("Category")

# Step 3: Select only the Amount column from each group
amount_column = grouped_data["Amount"]

# Step 4: Calculate total amount for each category
total_amount = amount_column.sum()

# Step 5: Convert index (Category) into a normal column
category_total = total_amount.reset_index()

print("\nMonthly Category-wise Expense Total:")
print(category_total.to_string(index=False))


# Step 6: Save the summary into a new Excel file
category_total.to_excel("C://Users//piyush kumar//Downloads//monthly_summary.xlsx", index=False)

print("\nmonthly_summary.xlsx created successfully.")