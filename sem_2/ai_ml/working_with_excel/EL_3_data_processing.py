'''      
--Data Preprocessing

1. Importing Libaries and Reading Cleaned Dataset

2. Label Encoding
• Label Encoder
• One hot Encoding
• Dummies

3. Feature Scaling
• MinMax Scaler
• Standard Scaler
• Binarizer

4. Feature Selection
• SelectKBest

5. Feature Extraction
• PCA

6. Train Test Split
'''

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler, Binarizer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.feature_selection import SelectKBest, f_classif , chi2
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split

df = pd.read_csv(r"C:\Users\piyush kumar\OneDrive\Desktop\GitHub\PESU\sem_2\ai_ml\working_with_excel\Salaries.csv")


# head() function in pandas is used to display the first few rows of a dataset
# By default, it shows the first 5 rows
# It helps to quickly understand the structure of the data
# You can pass a number inside head(n) to display n rows
# Example: df.head(10) will show the first 10 rows
# It is mainly used for previewing data before analysis
print(df.head())     # shows first 5 rows (default)
print(df.head(3))    # shows first 3 rows


print(df.info())# structure
print(df.describe())  # statistics
print(df.columns)     # column names

print(df.shape())


# ----------------- LabelEncoder-------------
'''
👉 You are converting categorical (text) data → numeric data using Label Encoding
👉 This is required because ML models only understand numbers
'''
le = LabelEncoder()

