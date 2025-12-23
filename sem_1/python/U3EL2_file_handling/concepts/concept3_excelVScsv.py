#--------------------------------------------- excel vs csv

# 🔹 CSV vs Excel (Key Difference)
'''
| Feature                      | CSV        | Excel (.xlsx)         |
| ---------------------------- | ---------- | --------------------- |
| File type                    | Plain text | Binary format         |
| Editable directly in VS Code | ✅ Yes      | ❌ No (not readable)   |
| Can be opened in Excel       | ✅          | ✅                     |
| Needs library                | `csv`      | `pandas` / `openpyxl` |
'''

# ------------------- csv
'''
🧪 CSV in VS Code (What you already know)

You can create:
students.csv

And type data manually:
RollNo,Name,Marks
1,Piyush,50
2,Rohit,60
'''

# ------------------- Excel
'''
🧪 Excel in VS Code (How it actually works)
❌ You CANNOT type Excel data like CSV

If you open attendance.xlsx in VS Code, you'll see:
PK���▒▒▒▒▒▒▒▒▒

👉 Because Excel is a binary file, not text


# how to create excel file:-

✅ Correct Way to Create Excel File
Option 1:- Create Excel using Excel / Google Sheets (BEST)

Open Excel
    Create attendance.xlsx
    Save it in same folder as Python file
    Access it in Python
    pd.read_excel("attendance.xlsx")



Option 2:- Create Excel using Python itself (LIKE CSV)

import pandas as pd

data = {
    "StudentID": [101, 102, 103],
    "Name": ["Piyush", "Rohit", "Aman"],
    "DaysPresent": [65, 80, 60],
    "TotalDays": [90, 90, 90]
}

df = pd.DataFrame(data)
df.to_excel("attendance.xlsx", index=False)

print("Excel file created")


👉 This is equivalent to manually creating CSV
'''

# NOTE
'''
🧠 Memory Trick

CSV → Text → VS Code
Excel → Binary → Library / Excel App
'''