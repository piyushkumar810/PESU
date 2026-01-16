import pandas as pd

data = {
    "Name": ["Piyush", "Amit", "Riya", "Neha", "Rahul"],
    "Age": [18, 19, 17, 18, 20],
    "Marks": [85, 90, 88, 92, 80]
}

df = pd.DataFrame(data)

# 1️⃣ df.head() – View first rows
# df.head() // by befault if value is not passed inside head function it will give all records
hed=df.head(3)
print(hed)

# 2️⃣ df.tail() – View last rows
tal=df.tail(2)
print(tal)
# ➡ Last 2 rows

# 3️⃣ df.shape – Size of DataFrame
shp=df.shape
print(shp)

# 4️⃣ df.columns – Column names
total_col=df.columns
print(total_col)
'''
Output:
Index(['Name', 'Age', 'Marks'], dtype='object')
'''

# 5️⃣ df.index – Index information
idx=df.index
print(idx)