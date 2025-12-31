'''
✅ Question 9

Compute the average unit price of products grouped by category.
'''

import pandas as pd

try:
   products_df = pd.read_csv("C://Users//piyush kumar//OneDrive//Desktop//GitHub//PESU//sem_1//python//U3EL2_file_handling//U3EL3_PANDAS//products.csv")
   print(products_df.columns)

   



except FileNotFoundError:
   print("invalid file")