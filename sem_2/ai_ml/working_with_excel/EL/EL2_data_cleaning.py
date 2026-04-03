'''
=========================================
        DATA CLEANING PIPELINE
=========================================

Steps covered:
1. Import libraries & load dataset
2. Drop unnecessary columns
3. Handle missing values
4. Remove duplicates
5. Detect & treat outliers
'''

# ================================
# 1. IMPORT LIBRARIES
# ================================

import pandas as pd     # For data manipulation
import numpy as np      # For numerical operations

# Load dataset into DataFrame
df = pd.read_csv(r"C:\Users\piyush kumar\OneDrive\Desktop\GitHub\PESU\sem_2\ai_ml\working_with_excel\EL_1\Salaries_updated.csv")

print(df.head())  # View first 5 rows


# ================================
# 2. DROPPING UNNECESSARY COLUMNS
# ================================

# 'Unnamed: 0' is usually an index column saved by mistake while exporting CSV
# axis=1 → column operation
# inplace=True → modify original DataFrame (no need to assign)

df.drop('Unnamed: 0', axis=1, inplace=True)


# ================================
# 3. MISSING VALUE TREATMENT
# ================================

# Check how many missing (null) values in each column
print(df.isnull().sum())


# -------------------------------
# Separate numerical & categorical columns
# -------------------------------

# Select columns with numeric datatype
numeric_cols = df.select_dtypes(include=np.number).columns

# Select non-numeric (categorical) columns
categorical_cols = df.select_dtypes(exclude=np.number).columns

print(numeric_cols)
print(categorical_cols)

print(df.dtypes)  # Show datatype of each column


# -------------------------------
# Fill missing values in NUMERIC columns
# -------------------------------

# Strategy: Fill with MEDIAN (robust to outliers)

for col in numeric_cols:
    if df[col].isnull().sum() > 0:   # Check if column has missing values
        
        # Replace null values with median of that column
        df[col] = df[col].fillna(df[col].median())


# -------------------------------
# Fill missing values in CATEGORICAL columns
# -------------------------------

# Strategy: Fill with MODE (most frequent value)

for col in categorical_cols:
    if df[col].isnull().sum() > 0:
        
        # mode()[0] → most frequent category
        df[col] = df[col].fillna(df[col].mode()[0])


# Check again to confirm no missing values left
print(df.isnull().sum())


# ================================
# 4. DUPLICATE REMOVAL
# ================================

# Count duplicate rows
duplicate_count = df.duplicated().sum()
print(duplicate_count)

# Remove duplicate rows
df = df.drop_duplicates()

# Verify duplicates removed
print(df.duplicated().sum())


# ================================
# 5. OUTLIER DETECTION & TREATMENT
# ================================

'''
We use IQR (Interquartile Range) method:

Q1 = 25th percentile
Q3 = 75th percentile
IQR = Q3 - Q1

Outlier condition:
value < Q1 - 1.5*IQR
value > Q3 + 1.5*IQR
'''

for col in numeric_cols:
    
    # Calculate quartiles
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    
    # Calculate IQR
    IQR = Q3 - Q1
    
    # Define bounds
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    # Identify outliers in this column
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]


# ⚠️ IMPORTANT NOTE:
# This loop overwrites 'outliers' each time
# So finally it only contains outliers from LAST column

print(outliers)        # Show detected outliers
print(outliers.index)  # Show their row indices


# Remove outlier rows from dataset
# axis=0 → row operation
df.drop(outliers.index, axis=0, inplace=True)

# ⚠️ drop() with inplace=True returns None
# so don't print it directly


# ================================
# 6. SAVE CLEANED DATA
# ================================

df.to_csv("salaries_cleaned.csv", index=False)

print("Cleaned dataset saved successfully")




# ------------------------------------✅ Correct Approach (BEST PRACTICE)
outlier_indices = set()

for col in numeric_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    # Collect indices
    indices = df[(df[col] < lower) | (df[col] > upper)].index
    outlier_indices.update(indices)

# Drop all outliers at once
df.drop(outlier_indices, inplace=True)

# 👉 Now it removes outliers from ALL columns correctly ✅


'''
🧠 INTERVIEW / GATE LEVEL UNDERSTANDING

🔥 Why MEDIAN for numeric?
Resistant to outliers
Better than mean in skewed data

🔥 Why MODE for categorical?
Most frequent value → logical replacement

🔥 Why remove duplicates?
Avoid bias in ML models

🔥 Why IQR method?
Standard statistical method
Works without assuming distribution
'''