'''
HADOOP + PYSPARK PRACTICAL (STEP-BY-STEP WITH EXPLANATION)

1. START ENVIRONMENT
   wsl -d bigdata-env
   su - hadoop
   → Opens Linux + switches to Hadoop user (required for big data tools)

2. CREATE CSV FILES
   nano customers.csv
   nano orders.csv
   nano employees.csv
   → Used to manually create datasets
   Save: CTRL+O → Enter → CTRL+X
   ls → verify files exist

3. START PYSPARK
   pyspark
   → Starts SparkSession (spark) and enters PySpark shell (>>>)

4. LOAD DATA (DATAFRAME CREATION)
   cust = spark.read.csv("file:///home/hadoop/customers.csv", header=True, inferSchema=True)
   order = spark.read.csv("file:///home/hadoop/orders.csv", header=True, inferSchema=True)
   emp   = spark.read.csv("file:///home/hadoop/employees.csv", header=True, inferSchema=True)
   → header=True → first row as column names
   → inferSchema=True → auto datatype detection

5. DISPLAY DATA
   cust.show()
   order.show()
   emp.show()
   → show() is an ACTION (executes Spark job and prints data)

6. COMMON ERRORS (IMPORTANT)
   CustomerID ❌ → customer_id ✅ (case-sensitive)
   orders ❌ → order ✅ (variable mismatch)
   pyspary ❌ → pyspark ✅ (wrong command)
   col not defined → from pyspark.sql.functions import *

7. JOINS (CORE CONCEPT)
   cust.join(order, "customer_id", "left")
   → LEFT JOIN → all customers + matching orders

   cust.join(order, "customer_id", "right")
   → RIGHT JOIN → all orders + matching customers

   cust.join(order, "customer_id", "inner")
   → INNER JOIN → only matching rows

   cust.join(order, "customer_id", "full")
   → FULL JOIN → all rows from both tables

   cust.join(order, "customer_id", "leftsemi")
   → LEFT SEMI → only customers having orders (left only)

   NOTE:
   → Duplicate rows = multiple orders per customer (1-to-many)
   → Duplicate columns = same column names in both tables

8. NULL HANDLING (VERY IMPORTANT)
   Problem: "NULL" in CSV is string, not actual NULL

   Fix:
   emp = emp.replace("NULL", None)

   Find NULL:
   emp.filter(col("age").isNull())

   Find NOT NULL:
   emp.filter(col("age").isNotNull())

   Multiple condition:
   emp.filter(col("age").isNotNull() & col("salary").isNotNull())

9. HANDLE NULL VALUES
   Add column with default:
   emp = emp.withColumn("final_salary", coalesce("salary", lit(100000)))
   → If salary NULL → replace with 100000

   Fill NULL:
   emp.na.fill({"department":"Unknown","experience":0})

   Drop NULL rows:
   emp.na.drop(how="any", subset=["age","salary"])

10. CREATE DATAFRAME MANUALLY
    data = [(101,"Aarav Sharma",28,45000,3),...]
    emp = spark.createDataFrame(data, ["emp_id","name","age","salary","experience"])
    → Used when no CSV available

11. OUTPUT HANDLING
    emp.show() → table format
    emp.collect() → list of Row objects
    Ctrl+C → stop execution
    exit() / Ctrl+D → exit PySpark

12. KEY CONCEPTS (EXAM IMPORTANT)
    → PySpark is case-sensitive
    → Joins create combinations (Cartesian effect)
    → NULL ≠ "NULL"
    → show() triggers execution (action)
    → withColumn() adds/modifies column
    → na.fill() replaces NULL
    → na.drop() removes NULL rows

END
'''