import numpy as np
import pandas as pd

emp_names = ["Piyush", "Rahul", "Ankit", "Priya", "Sneha"]

print(emp_names)
df=pd.DataFrame(emp_names)

df.columns=['Employee_Name']
print(df)
print()

data={'Name':["Piyush", "Rahul", "Ankit", "Priya",],
      'Age':[23,22,22,21]}
df_dict=pd.DataFrame(data)
print(df_dict)