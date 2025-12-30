'''
✅ Question 5

Management wants to see only Corporate customers.
Filter the customers DataFrame to show Corporate segment customers.
'''

import pandas as pd

try:
    customers_df=pd.read_csv("C://Users//piyush kumar//OneDrive//Desktop//GitHub//PESU//sem_1//python//U3EL2_file_handling//U3EL3_PANDAS//customer.csv")
    # print(customers_df)

    Corporate_customers=customers_df[customers_df["segment"]=="Corporate"]
    print(Corporate_customers)


except Exception as e:
    print("msg",e)