'''
Question 11

Merge orders with products to calculate order value for each order line.
Order value is quantity multiplied by unit_price.
'''

import pandas as pd

try:
    read_product=pd.read_csv("C:\\Users\\piyush kumar\\OneDrive\\Desktop\\GitHub\\PESU\\sem_1\\python\\U3EL2_file_handling\\U3EL3_PANDAS\\orders.csv")
    read_order=pd.read_csv("C://Users//piyush kumar//OneDrive//Desktop//GitHub//PESU//sem_1//python//U3EL2_file_handling//U3EL3_PANDAS//products.csv")

    print(read_order.columns)
    print(read_product.columns)
except FileNotFoundError:
    print("invalid file")
