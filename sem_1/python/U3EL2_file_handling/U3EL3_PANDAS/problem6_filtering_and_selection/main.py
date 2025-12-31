'''
✅ Question 6

Identify all orders where quantity is greater than 10.
Display order_id, customer_id, and quantity.
'''

import pandas as pd
try:
    order_df=pd.read_csv("C://Users//piyush kumar//OneDrive//Desktop//GitHub//PESU//sem_1//python//U3EL2_file_handling//U3EL3_PANDAS//orders.csv")
    # print(order_df)
    print(order_df.columns)

    custome_order=order_df[order_df["quantity"]>10]

    result=custome_order[['order_id','customer_id','quantity']]
    print(result)


except FileNotFoundError:
    print("invalid file")


# ------------------------- concept behind using double brackets (result in program)------------------
'''
Short Answer:
👉 Because we are selecting MULTIPLE columns, and Pandas expects a list of column names.


🧠 Deep Understanding (Step by Step)

1️⃣ Single square bracket → select ONE column
orders_df["OrderID"]

✔ Output type: Series
✔ Only one column


2️⃣ Double square bracket → select MULTIPLE columns
orders_df[["OrderID", "CustomerID", "Quantity"]]

✔ Output type: DataFrame
✔ Multiple columns together
'''
# -----------------------------------------
'''
📦 What do the two brackets actually mean?
orders_df[  ["OrderID", "CustomerID", "Quantity"]  ]
      ↑            ↑
   DataFrame     list of columns


Outer [] → Pandas indexing
Inner [] → Python list
'''