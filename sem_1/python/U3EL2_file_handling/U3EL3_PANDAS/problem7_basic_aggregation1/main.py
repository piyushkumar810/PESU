'''
✅ Question 7

Find the total quantity ordered for each product_id.
Sort the result in descending order of quantity.
'''

import pandas as pd

try:
    order_df=pd.read_csv("C://Users//piyush kumar//OneDrive//Desktop//GitHub//PESU//sem_1//python//U3EL2_file_handling//U3EL3_PANDAS//orders.csv")
    print(order_df.columns)

    # total_qnt=0
    # for qnt_data in order_df["quantity"]:
    #     total_qnt=total_qnt+qnt_data
    # print(total_qnt)

    ## Calculate total quantity per product
    product_quantity = (
    order_df.groupby("product_id")["quantity"]
    .sum()
    .reset_index()
    )
    
    ## Sort in descending order of quantity
    product_quantity_sorted = product_quantity.sort_values(
    by="quantity",
    ascending=False
    )

    print(product_quantity_sorted)

except FileNotFoundError:
    print("invalid file")


# -------------------------- UNDERSTANDING GROUP BY

# This is your Orders DataFrame.
'''
| OrderID | ProductID | Quantity |
| ------- | --------- | -------- |
| 1       | P101      | 5        |
| 2       | P102      | 10       |
| 3       | P101      | 7        |
| 4       | P103      | 20       |
| 5       | P102      | 3        |
'''

# explanation
#  product_quantity = (
#     order_df.groupby("product_id")["quantity"]
#     .sum()
#     .reset_index()
#     )
'''
2️⃣.groupby("ProductID")
🔹 What it does:

👉 Groups rows that have the same ProductID
Think of it like:

“Put all P101 orders together, all P102 together, etc.”

After grouping:

Group P101 → quantities [5, 7]
Group P102 → quantities [10, 3]
Group P103 → quantities [20]

📌 No calculation yet, just grouping.

3️⃣ ["Quantity"]
🔹 What it does:

👉 From each product group, select only the Quantity column

We don’t care about OrderID now.

So it becomes:

P101 → [5, 7]
P102 → [10, 3]
P103 → [20]

4️⃣ .sum()
🔹 What it does:

👉 Adds quantities inside each group

Calculation:
P101 → 5 + 7 = 12
P102 → 10 + 3 = 13
P103 → 20

Result at this stage:

5️⃣ .reset_index()
🔹 Why is this needed?

Right now:
ProductID is the index
Quantity is the value
But we want a proper DataFrame.

🔹 What it does:

👉 Converts index into a normal column

Final output:

ProductID	Quantity
P101	12
P102	13
P103	20

✔ Now it’s a clean DataFrame
✔ Easy to sort, merge, export

🧩 Why parentheses ( ) ?
product_quantity = (
    orders_df
    .groupby(...)
    .sum()
)


✔ Used for method chaining
✔ Makes code readable
✔ Avoids long single line
'''



# ------------ one more concept
'''
🔍 The line in question
.groupby("product_id")["quantity"]


You’re asking:
Why round brackets () here and square brackets [] here?

🧠 Short Answer
Round brackets () → used for function / method calls
Square brackets [] → used for selecting data (indexing)


groupby("product_id")
👉 Means:

“Call the groupby method and pass "product_id" as input”

and then

["quantity"]
👉 Means:

“From the grouped data, select the quantity column”


🔗 Combined Meaning
orders_df.groupby("product_id")["quantity"]

Read it like English:
“Group the data by product_id, then select the quantity column.”
'''