# ================================
# 1. IMPORTING LIBRARY
# ================================

import pandas as pd  # Import pandas and give it alias 'pd'
print("Pandas imported successfully")


# ================================
# 2. LOADING DATASET
# ================================

# Read CSV file into a DataFrame
df = pd.read_csv(r"C:\Users\piyush kumar\OneDrive\Desktop\GitHub\PESU\sem_2\ai_ml\working_with_excel\EL_1\Salaries.csv")

# print(df)  # Uncomment to see full dataset


# ================================
# 3. INITIAL INSPECTION
# ================================

print(df.head())       # First 5 rows (default)
print(df.head(10))     # First 10 rows

print(df.tail())       # Last 5 rows

print(df.shape)        # (rows, columns)

print(df.columns)      # Column names

print(df.dtypes)       # Data type of each column

print(df.info())       # Structure + non-null count + datatypes

print(df.describe())   # Summary stats for numerical columns

print(df.describe(include="all"))  # Summary for ALL columns


# ================================
# 🔥 4. ROW RETRIEVAL (IMPORTANT)
# ================================

# 👉 iloc = INTEGER LOCATION (index-based)
# 👉 Works like array indexing (0,1,2,...)

print(df.iloc[0])        # First row
print(df.iloc[2])        # Third row
print(df.iloc[11:16])    # Rows from index 11 to 15
print(df.iloc[[2,4,6]])  # Specific rows


# ================================
# 🔥 loc vs iloc (CORE CONCEPT)
# ================================

"""
👉 iloc → uses POSITION (numbers)
   Example: df.iloc[0] → first row

👉 loc → uses LABEL (actual index name)
   Example: df.loc[0] → row with index label 0

⚠️ Difference:
iloc → exclusive slicing (like Python)
loc → inclusive slicing
"""

# Example:
# df.iloc[0:3] → rows 0,1,2
# df.loc[0:3] → rows 0,1,2,3


# ================================
# 5. COLUMN RETRIEVAL
# ================================

print(df["salary"])              # Single column (Series)

print(df[["rank", "salary"]])    # Multiple columns (DataFrame)

# Using iloc for columns (position-based)
print(df.iloc[:, 1:4])           # Columns index 1 to 3
print(df.iloc[:, [1,4,5]])       # Specific columns


# ================================
# 6. ADDING NEW ROW
# ================================

new_row = {
    "rank": "AsstProf",
    "discipline": "A",
    "yrs.since.phd": 8,
    "yrs.service": 5,
    "sex": "Female",
    "salary": 85000
}

# Add row at last index
df.loc[len(df)] = new_row

print(df.tail())  # Check last rows


# ================================
# 7. ADDING NEW COLUMN
# ================================

# Create new column based on existing column
df["salary_in_lakhs"] = df["salary"] / 100000

print(df.head())


# ================================
# 8. SUBSETTING
# ================================

# Select first 10 rows and first 4 columns
sl = df.iloc[0:10, 0:4]
print(sl)

# Select specific columns
s2 = df[["rank", "sex", "salary"]]
print(s2.head())

# Select rows 5 to 10 with selected columns
print(df.loc[5:10, ["rank", "yrs.service", "salary"]])


# ================================
# 🔥 9. FILTERING (VERY IMPORTANT)
# ================================

# Numerical filtering
high_salary = df[df["salary"] > 120000]
print(high_salary)

# Categorical filtering
prof = df[df["rank"] == "Prof"]
print(prof)

# Multiple conditions
filtered_data = df[(df["rank"] == "Prof") & (df["salary"] > 130000)]
print(filtered_data)


# ================================
# 10. SORTING
# ================================

print(df.sort_values(by="salary"))  # Ascending
print(df.sort_values(by="salary", ascending=False))  # Descending


# ================================
# 11. AGGREGATE FUNCTIONS
# ================================

print(df["salary"].mean())          # Mean
print(df["salary"].mean().round(2)) # Rounded mean

print(df["salary"].max())           # Maximum
print(df["salary"].min())           # Minimum

print(df["sex"].unique())           # Unique values

print(df["sex"].value_counts())     # Frequency count


# ================================
# 12. SAVING FILE
# ================================

df.to_csv("Salaries_updated.csv", index=False)
print("File saved successfully")


#------------------------------------------ 🚀 BONUS (VERY IMPORTANT — I ADDED FOR YOU)

# # 🔥 GroupBy (MUST KNOW)
# print(df.groupby("rank")["salary"].mean())
# # 👉 Average salary per rank


# # 🔥 Missing Values Handling
# print(df.isnull().sum())   # Check missing values

# df = df.dropna()          # Remove missing rows

# # 🔥 Rename Columns
# df.rename(columns={"salary": "Salary"}, inplace=True)

# # 🔥 Apply Function
# df["salary_double"] = df["salary"].apply(lambda x: x*2)