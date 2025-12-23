# question
'''
📘 Problem Statement 5: Product Inventory Check Using CSV
Question

Write a Python program to check product inventory using a CSV file.

A CSV file named inventory.csv contains the following columns:
ProductID, ProductName, Stock, ReorderLevel.

The program should perform the following tasks:
    Read the CSV file sequentially from disk.
    Identify products whose Stock is below the ReorderLevel.
    Create a new CSV file named reorder_list.csv.
    Write only the following details into the new file:
        ProductID
        ProductName
        Stock
'''
import csv

with open("C://Users//piyush kumar//OneDrive//Desktop//GitHub//PESU//sem_1//python//U3EL2_file_handling//problem5_product_inventory_check//inventory.csv","r",newline="") as file:
    reader=csv.DictReader(file)

    # for row in reader:
    #     # print(row)

    with open("C://Users//piyush kumar//OneDrive//Desktop//GitHub//PESU//sem_1//python//U3EL2_file_handling//problem5_product_inventory_check//reorder_list.csv","w",newline="") as file:
        fieldsnames=["ProductID","ProductName","Stock"]

        writer=csv.DictWriter(file,fieldnames=fieldsnames)
        writer.writeheader()

        for row in reader:
            stock=int(row["Stock"])
            reorder_level = int(row["ReorderLevel"])

            if stock<reorder_level:
                writer.writerow({
                    "ProductID": row["ProductID"],
                    "ProductName":row["ProductName"],
                    "Stock":row["Stock"]
                })

print("reorder_list.csv created successfully.")
