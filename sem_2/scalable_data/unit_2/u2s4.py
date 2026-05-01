'''
🚀 🧠 COMPLETE FLOW
CMD → Start Spark → Load Data → DataFrame → SQL → DDL → DML


💻 STEP 0: PREPARE DATA FILE
Create file:
nano sales.txt

Paste this (your data):

101,Phone,Electronics,45000
102,Laptop,Electronics,75000
103,Tablet,Electronics,30000
104,Smartwatch,Electronics,12000
105,Headphones,Electronics,5000

Save → CTRL+X → Y → Enter


💻 STEP 1: START PYSPARK
pyspark

👉 You should see:
>>>


💻 STEP 2: CREATE DATAFRAME
df = spark.read.csv("sales.txt", header=False, inferSchema=True)
df = df.toDF("orderId","product","category","amount")


💻 STEP 3: CHECK DATA
df.show()
df.printSchema()

🧠 Output
+-------+---------+-----------+------+
|orderId|product  |category   |amount|
+-------+---------+-----------+------+


💻 STEP 4: BASIC OPERATIONS
✔ Select
df.select("product","amount").show()
✔ Filter
df.filter(df.amount > 20000).show()
✔ GroupBy
df.groupBy("category").sum("amount").show()


💻 STEP 5: USE SQL
🔹 Create temp view
df.createOrReplaceTempView("sales")

🔹 Run SQL
spark.sql("SELECT * FROM sales").show()

🔹 Aggregation
spark.sql("""
SELECT category, SUM(amount)
FROM sales
GROUP BY category
""").show()


💻 STEP 6: DDL OPERATIONS
✔ Create database
spark.sql("CREATE DATABASE IF NOT EXISTS retail")

✔ Use database
spark.sql("USE retail")

✔ Create table
spark.sql("""
CREATE TABLE sales_table (
    product STRING,
    category STRING,
    amount INT
)
USING parquet
""")


💻 STEP 7: DML OPERATIONS
✔ INSERT
spark.sql("""
INSERT INTO sales_table VALUES
('Phone','Electronics',45000)
""")

✔ SELECT
spark.sql("SELECT * FROM sales_table").show()

✔ FILTER
spark.sql("""
SELECT * FROM sales_table
WHERE amount > 20000
""").show()


💻 STEP 8: DROP TABLE
spark.sql("DROP TABLE IF EXISTS sales_table")

'''