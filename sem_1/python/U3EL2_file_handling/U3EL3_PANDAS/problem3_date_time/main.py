'''
✅ Question 3

Order dates are stored as strings.
Tasks:

Convert the order_date column into datetime format
Verify the datatype change
'''

import pandas as pd
try:
    orders_df = pd.read_csv("C://Users//piyush kumar//OneDrive//Desktop//GitHub//PESU//sem_1//python//U3EL2_file_handling//U3EL3_PANDAS//orders.csv")
    # print(orders_df)

    print(orders_df.dtypes)

    orders_df["order_date"] = pd.to_datetime(orders_df["order_date"])
    print(orders_df.dtypes)


except FileNotFoundError:
    print("invalid file")

'''
🧠 Exam-Friendly Explanation

CSV files store dates as strings:-
Pandas treats them as object type

pd.to_datetime() converts them into datetime64
Datetime format enables:
Sorting by date
Date filtering
Time-based analysis

✅ Final One-Line Answer (For Exams)

The order_date column was converted from string (object) to datetime64[ns] using pd.to_datetime(),
 and the datatype change was verified using dtypes.
'''