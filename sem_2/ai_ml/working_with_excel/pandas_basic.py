import pandas as pd

# Load dataset
file_path = r'C:\Users\piyush kumar\OneDrive\Desktop\GitHub\PESU\sem_2\ai_ml\working_with_excel\Salaries.csv'
df = pd.read_csv(file_path)

# 1. Display full dataset
print("📊 DATASET:")
print(df)

# 2. Column names
print("\n📌 COLUMNS:")
print(df.columns)

# 3. Data types of each column
print("\n📌 DATA TYPES:")
print(df.dtypes)

# 4. Info (structure of dataset)
print("\n📌 INFO:")
df.info()   # No need to print() because info() already prints

# 5. Statistical summary (numerical only)
print("\n📌 NUMERICAL SUMMARY:")
print(df.describe())

# 6. Statistical summary (all columns)
print("\n📌 FULL SUMMARY (INCLUDING CATEGORICAL):")
print(df.describe(include="all"))

# Selects the first row (index = 0)
# Output → A Series (single row with all column values)
print(df.iloc[0])


# Selects rows from index 11 to 15
# Note: 16 is excluded (Python slicing rule)
# Output → A DataFrame containing 5 rows (11,12,13,14,15)
print(df.iloc[11:16])


# ❌ WRONG SYNTAX
# iloc expects at most TWO arguments → [rows, columns]
# Here you gave 3 arguments → (2,4,6) → this will give ERROR

# ✔ Correct versions:

# Select row index 2 and column index 4 → single value
# print(df.iloc[2, 4])

# Select multiple rows (2,4,6) → all columns
print(df.iloc[[2, 4, 6]])

# Select row index 2 and multiple columns (4,6)
# print(df.iloc[2, [4, 6]])

# retrieve column by column position
print(df.iloc[:,1:4])

# 
print(df.iloc[:,[1,4,5]])

# creating new row
new_row = {
    'EmployeeName': 'John',
    'JobTitle': 'Manager',
    'BasePay': 50000,
    'OvertimePay': 5000,
    'OtherPay': 2000
}

# insert row
df.loc[len(df)] = new_row

print(df.tail())



# filtering
# high_salary

# saving the dataset
