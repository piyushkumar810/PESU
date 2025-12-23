# question
'''
📘 Problem Statement 4: Employee Salary Update Using Excel
Question

Write a Python program to update employee salary details using an Excel file.

An Excel file named emp_data.xlsx is available with the following columns:
EmpID, Name, BasicSalary, Department.

The program should perform the following tasks:
    
    Read the Excel file from disk.
        Calculate:
        
        HRA = 10% of BasicSalary
        DA = 18% of BasicSalary
    
    Compute the GrossSalary using the formula:
        GrossSalary = BasicSalary + HRA + DA
    
    Create a new Excel file named emp_salary.xlsx.
    Write only the following columns into the new file:
        EmpID
        Name
        GrossSalary
'''

import pandas as pd

data={
    "EmpID": [101, 102, 103, 104],
    "Name": ["Piyush", "Rohit", "Aman", "Neha"],
    "BasicSalary":[30000,40000,25000,50000],
    "Department": ["IT","HR","Finance","IT"]
}

df=pd.DataFrame(data)
# print(df)  # this will give index also if you dont want then use df.to_string(index=False)
print(df.to_string(index=False))
'''
👉 to_string() is a pandas method that converts a DataFrame into a formatted string.
            It does not change the DataFrame
            It only changes how it is displayed
            Used mainly for printing / viewing
'''

'''
✅ Recommended Practice (Lab)

Situation	                         Use
-------------------------------------------------------------
Console display	                    to_string(index=False)
Excel / CSV output               	index=False
'''

df["HRA"]=df["BasicSalary"]*0.10
df["DA"]=df["BasicSalary"]*0.18

df["GrossSalary"]=df["BasicSalary"]+df["HRA"]+df["DA"]

result_df=df[["EmpID","Name","GrossSalary"]]
print()
print("----------- final incremental salary calculation------------")
print(result_df.to_string(index=False))