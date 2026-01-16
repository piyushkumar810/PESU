# ------------------------a pandas dataframe can be created 

# 1️⃣ Creating DataFrame using Python Dictionary
import pandas as pd

data = {
    "Name": ["Piyush", "Amit", "Riya"],
    "Age": [18, 19, 17],
    "Marks": [85, 90, 88]
}

df = pd.DataFrame(data)
print(df)
# 📌 Most common & important method


# 2️⃣ Creating DataFrame using Python List
import pandas as pd

data = [
    ["Piyush", 18, 85],
    ["Amit", 19, 90],
    ["Riya", 17, 88]
]

df = pd.DataFrame(data, columns=["Name", "Age", "Marks"])
print(df)


# 3️⃣ Creating DataFrame from a File
# Example: From CSV file
import pandas as pd

df = pd.read_csv("C:\\Users\\piyush kumar\\OneDrive\\Desktop\\GitHub\\PESU\\sem_1\\python\\csv_file\\file.csv")
print(df)
'''
📌 Common file functions:
read_csv()
read_excel()
read_json()
'''

# 4️⃣ Creating an Empty DataFrame
import pandas as pd

df = pd.DataFrame()
print(df)

'''
🧠 Easy memory table (for exams)
Method	            Function
Dictionary	       pd.DataFrame(dict)
List	           pd.DataFrame(list)
File	           pd.read_csv()
Empty	           pd.DataFrame()
'''



# ---------------------------- looking at some functions of dataFrame
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

'''
Output:
RangeIndex(start=0, stop=5, step=1)
'''
# 🧠 Index starts from 0 to 4


# 📌 Exam-ready summary table
'''
Function	Purpose
df.head()	Shows first rows
df.tail()	Shows last rows
df.shape	(rows, columns)
df.columns	Column names
df.index	Index values

✍️ One-line exam answers
head() → Displays first few rows
tail() → Displays last few rows
shape → Returns number of rows and columns
columns → Returns column names
index → Returns index of DataFrame
'''

