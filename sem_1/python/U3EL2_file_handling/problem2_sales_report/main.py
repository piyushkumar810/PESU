# question
'''
Write a Python program to generate a sales report from a CSV file.

A CSV file named daily_sales.csv is stored in a folder with the following columns:
Date, Product, Region, Quantity, Amount.

The program should perform the following tasks:

    Read the CSV file line by line from disk.
    Compute the total sales amount for each Region.
    Create a new CSV file named region_sales.csv.
    Store only those regions whose total sales amount is 50,000 or above.
    Exclude regions with total sales below 50,000 from the output file.
'''

import csv
region_sales={}

with open("C://Users//piyush kumar//OneDrive//Desktop//GitHub//PESU//sem_1//python//U3EL2_file_handling//problem2_sales_report//daily_sales.csv","r",newline="")as file:
    reader=csv.DictReader(file)

    for row in reader:
        # print(row)
        #  i want this two only region and amount and if region appred multiple time then amount will be added
        region=row["Region"]
        amount=float(row["Amount"])

        if region not in region_sales:
            region_sales[region]=amount
            # print(region_sales[region])
        else:
            region_sales[region]+=amount

# now we will create another csv file which wil store Store only those regions whose total sales amount is 50,000 or above.
with open("C://Users//piyush kumar//OneDrive//Desktop//GitHub//PESU//sem_1//python//U3EL2_file_handling//problem2_sales_report//region_sales.csv","w",newline="")as file:
    fieldnames = ["Region", "TotalSales"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    for region, total in region_sales.items():
        if total >= 50000:   # Exclude regions below 50000
            writer.writerow({
                "Region": region,
                "TotalSales": total
            })

    # ------------------ this is the another method-------------------
    # writer=csv.writer(file)

    # writer.writerow(["Region","TotalSalesAmount"])

    # for region,total in region_sales.items():
    #     if total>=50000:
    #         writer.writerow([region,total])

print("region_sales.csv file created successfuly")



# ------------vvi--------------- difference between these two methods---------------vvi------------

# -------------------- First Method: csv.DictWriter-----------------

# fieldnames = ["Region", "TotalSales"]
# writer = csv.DictWriter(file, fieldnames=fieldnames)

# writer.writeheader()

# for region, total in region_sales.items():
#     if total >= 50000:
#         writer.writerow({
#             "Region": region,
#             "TotalSales": total
#         })
'''
explanation:- 

✅ How it works

    Writes data using dictionary keys
    Column order is controlled by fieldnames
    Safer and more readable
    Best for structured data

| Feature           | DictWriter |
| ----------------- | ---------- |
| Uses dictionaries | ✅          |
| Uses column names | ✅          |
| Order controlled  | ✅          |
| Readable & safe   | ✅          |

⚠️ Important
Keys in dictionary must match fieldnames
Otherwise → error or missing data

'''

# ----------------------- Second Method: csv.writer-----------------
# writer = csv.writer(file)

# writer.writerow(["Region", "TotalSalesAmount"])

# for region, total in region_sales.items():
#     if total >= 50000:
#         writer.writerow([region, total])

'''
explanation:-
✅ How it works

    Writes lists/tuples
    No column-name checking
    Faster and simpler
    Best for simple output

| Feature           | writer |
| ----------------- | ------ |
| Uses lists        | ✅      |
| Uses column names | ❌      |
| Order matters     | ✅      |
| Less safe         | ❌      |


# -------------------- clear difference between those two---------------

| Aspect           | DictWriter      | writer      |
| ---------------- | --------------- | ----------- |
| Data format      | Dictionary      | List        |
| Column safety    | High            | Low         |
| Readability      | High            | Medium      |
| Error protection | Yes             | No          |
| Best for         | Structured data | Simple data |
| Exam preference  | ⭐⭐⭐         | ⭐⭐       |


--------------------------------🧠 Example Difference
DictWriter (Key-based)
writer.writerow({"Region": "North", "TotalSales": 60000})
✔ Order does not matter
✔ Column names guaranteed


writer (Position-based)
writer.writerow(["North", 60000])
⚠️ Order must be correct
⚠️ Easy to mix columns
'''