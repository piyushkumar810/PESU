'''
✅ Question 4

Analyze only South region orders.
Task:

Filter the orders DataFrame to show records from the South region.
'''

import pandas as pd

try:
    orders_df=pd.read_csv("C://Users//piyush kumar//OneDrive//Desktop//GitHub//PESU//sem_1//python//U3EL2_file_handling//U3EL3_PANDAS//orders.csv")
    # print(orders_df)

    # print(orders_df.columns)

    south_orders = orders_df[orders_df["region"] == "South"]
    print(south_orders)

except Exception as e:
    print("msg",e)