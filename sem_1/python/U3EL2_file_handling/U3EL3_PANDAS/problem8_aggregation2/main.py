'''
✅ Question 8

Calculate the number of orders placed in each region.
Display region and order count.
'''

import pandas as pd

try:
    order_df=pd.read_csv("C://Users//piyush kumar//OneDrive//Desktop//GitHub//PESU//sem_1//python//U3EL2_file_handling//U3EL3_PANDAS//orders.csv")
    print(order_df.columns)

    region_order_count=(
        order_df.groupby("region")
        .size()
        # .reset_index(name="order_count")
    )
    
    print(region_order_count)

except FileNotFoundError:
    print("invalid file")
