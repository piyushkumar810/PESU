# ✅ Question 2
'''
Column names contain mixed casing and spacing risks.
Tasks:

Inspect column names for consistency
(inspect means=check+observe+understand)
List all column names for each DataFrame
'''

import pandas as pd

try:
    customers_df = pd.read_csv("C://Users//piyush kumar//OneDrive//Desktop//GitHub//PESU//sem_1//python//U3EL2_file_handling//U3EL3_PANDAS//customer.csv")
    products_df = pd.read_csv("C://Users//piyush kumar//OneDrive//Desktop//GitHub//PESU//sem_1//python//U3EL2_file_handling//U3EL3_PANDAS//products.csv")
    orders_df = pd.read_csv("C://Users//piyush kumar//OneDrive//Desktop//GitHub//PESU//sem_1//python//U3EL2_file_handling//U3EL3_PANDAS//orders.csv")
    payments_df = pd.read_csv("C://Users//piyush kumar//OneDrive//Desktop//GitHub//PESU//sem_1//python//U3EL2_file_handling//U3EL3_PANDAS//payment.csv")

    print("customers_df column names = ",customers_df.columns)
    print("products_df column names = ",products_df.columns)
    print("orders_df column names = ",orders_df.columns)
    print("payments_df column names = ",payments_df.columns)

except FileNotFoundError:
    print("invalid file")


# -------------------------------summary ----------------------------
# .columns -> gives column field names of your csv file