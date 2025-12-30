# ✅ Problem Statement
'''
Given four CSV files representing:

Customers
Products
Orders
Payments

Tasks:
Load all CSV files into Pandas DataFrames
Display the number of rows and columns for each DataFrame
'''

import pandas as pd

# customer_df=pd.read_csv("C://Users//piyush kumar//OneDrive//Desktop//GitHub//PESU//sem_1//python//U3EL2_file_handling//U3EL3_fille_handling//customer.csv","r")
'''
error:-
❌ Problem 1: "r" is NOT needed
"r" is used with open()

pd.read_csv() does NOT accept file mode
'''

# for row in customer_df:
#     print(row)
'''
It prints column names, NOT rows.
'''

# if you want to print full row data
try:
    customers_df = pd.read_csv("C://Users//piyush kumar//OneDrive//Desktop//GitHub//PESU//sem_1//python//U3EL2_file_handling//U3EL3_fille_handling//customer.csv")

    # for index, row in customers_df.iterrows():
    #     print(row)
    for x in customers_df:
        print(x)
except FileNotFoundError:
    print("invalid file")


'''
| Code            | Meaning                             |
| --------------- | ----------------------------------- |
| `pd.read_csv()` | Reads CSV into DataFrame            |
| `for x in df`   | Iterates column names               |
| `df.iterrows()` | Iterates row by row                 |
| `"r"`           | Used only with `open()`, NOT pandas |

'''


# ----------------------- real question solution ------------------------

# Load CSV files into DataFrames
customers_df = pd.read_csv("C://Users//piyush kumar//OneDrive//Desktop//GitHub//PESU//sem_1//python//U3EL2_file_handling//U3EL3_fille_handling//customer.csv")
products_df = pd.read_csv("C://Users//piyush kumar//OneDrive//Desktop//GitHub//PESU//sem_1//python//U3EL2_file_handling//U3EL3_fille_handling//products.csv")
orders_df = pd.read_csv("C://Users//piyush kumar//OneDrive//Desktop//GitHub//PESU//sem_1//python//U3EL2_file_handling//U3EL3_fille_handling//orders.csv")
payments_df = pd.read_csv("C://Users//piyush kumar//OneDrive//Desktop//GitHub//PESU//sem_1//python//U3EL2_file_handling//U3EL3_fille_handling//payment.csv")

# Display number of rows and columns
print("Customers DataFrame:", customers_df.shape)
print("Products DataFrame:", products_df.shape)
print("Orders DataFrame:", orders_df.shape)
print("Payments DataFrame:", payments_df.shape)

# --------------------- summary ------------------
'''shape object is used to count no of rows and columns of your file'''