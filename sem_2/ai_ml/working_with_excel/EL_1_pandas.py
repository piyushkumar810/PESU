import pandas as pd

data={
    "name":["piyush", "navya", "prabhat"],
    "score":[60,70,80],
    "city":["jharkhand","bangalor","bihar"]
}

df=pd.DataFrame(data)
# print(df)

# 2. Loading Dataset
df1=pd.read_csv(r"C:\Users\piyush kumar\OneDrive\Desktop\GitHub\PESU\sem_2\ai_ml\working_with_excel\Salaries.csv")
print(df1)

# Display first 5 rows
print(df.head())

# Display last 5 rows
print(df.tail())

# display 10 rows
print(df.head(10))

# Check the shape of the dataset -> (rows,columns)
print(df.shape)

# Check column names
print(df.columns)

# Check data types
print(df.dtypes)

# General information
print(df.info())

# Statistical summary of numerical columns
print(df.describe())

