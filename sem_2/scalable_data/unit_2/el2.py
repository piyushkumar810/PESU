
'''
# ================================
# STEP 0: START PYSPARK
# ================================
# Run in CMD:
# pyspark


# ================================
# STEP 1: READ CSV + JSON DATA
# ================================
from pyspark.sql import functions as F

# Read CSV
df_csv = spark.read.csv(
    "orders.csv",
    header=True,
    inferSchema=True
)

# Read JSON
df_json = spark.read.json("orders.json")

# Combine both datasets
df = df_csv.unionByName(df_json)

df.show()


# ================================
# STEP 2: CREATE TEMP VIEW
# ================================
df.createOrReplaceTempView("orders")


# ================================
# STEP 3: DDL OPERATIONS (SQL)
# ================================

# Create database
spark.sql("CREATE DATABASE IF NOT EXISTS sales_db")

# Use database
spark.sql("USE sales_db")

# Create table
spark.sql("""
CREATE TABLE IF NOT EXISTS orders_tbl (
    order_id STRING,
    customer_id STRING,
    city STRING,
    order_date STRING,
    amount DOUBLE,
    status STRING
)
USING PARQUET
""")


# ================================
# STEP 4: DML OPERATIONS
# ================================

# DataFrame API
df_filtered = df.filter(F.col("amount") > 10000) \
                .select("order_id", "city", "amount")

df_filtered.show()


# SQL Equivalent
spark.sql("""
SELECT order_id, city, amount
FROM orders
WHERE amount > 10000
""").show()


# ================================
# STEP 5: AGGREGATIONS
# ================================

# DataFrame API
df.groupBy("city").agg(
    F.sum("amount").alias("total_revenue")
).show()

# SQL
spark.sql("""
SELECT city, SUM(amount) AS total_revenue
FROM orders
GROUP BY city
""").show()


# ================================
# STEP 6: CREATE PARTITIONED TABLE
# ================================

spark.sql("""
CREATE TABLE IF NOT EXISTS orders_part (
    order_id STRING,
    customer_id STRING,
    city STRING,
    amount DOUBLE,
    status STRING
)
USING PARQUET
PARTITIONED BY (order_date)
""")


# ================================
# STEP 7: WRITE DATA INTO PARTITIONED TABLE
# ================================

df.write.mode("overwrite") \
  .partitionBy("order_date") \
  .saveAsTable("orders_part")


# ================================
# STEP 8: QUERY PARTITIONED TABLE
# ================================

# With partition filter (FAST)
spark.sql("""
SELECT * FROM orders_part
WHERE order_date = '2026-02-04'
""").show()

# Without partition filter (SLOW)
spark.sql("""
SELECT * FROM orders_part
""").show()

'''