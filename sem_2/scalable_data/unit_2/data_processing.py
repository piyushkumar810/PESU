'''python
# ============================================
# 🌳 HADOOP + PYSPARK COMPLETE FLOW (SCRIPT)
# ============================================

# ==============================
# 1. ENVIRONMENT SETUP (THEORY)
# ==============================

# Install Java → required for Hadoop & Spark (runs on JVM)
# Install Python → required for PySpark
# Install WSL → Linux inside Windows (used in real Hadoop setup)
# Install Hadoop:
#   - HDFS → storage system (distributed)
#   - MapReduce → old processing model
# Install Spark:
#   - Faster than MapReduce
#   - In-memory processing

# ==============================
# 2. START ENVIRONMENT
# ==============================

# In CMD:
# pyspark

# SparkSession is automatically created:
# spark → entry point for all operations


# ==============================
# 3. LOAD DATA (CSV → DataFrame)
# ==============================

df = spark.read.csv(
    "file:///C:/data/movies.csv",
    header=True,
    inferSchema=True
)

# spark.read.csv → reads file into DataFrame
# header=True → first row = column names
# inferSchema=True → auto detect data types
# DataFrame = distributed table (like SQL but big data)


# ==============================
# 4. DATAFRAME OPERATIONS
# ==============================


# --------------------------------
# show() → display data
# --------------------------------
df.show()

# ACTION → triggers execution
# Displays first 20 rows
# Spark uses LAZY EVALUATION → executes only here


# --------------------------------
# printSchema() → structure
# --------------------------------
df.printSchema()

# Shows:
# column name + data type
# Helps understand dataset


# --------------------------------
# count() → total rows
# --------------------------------
df.count()

# ACTION → scans entire dataset
# Expensive in big data


# --------------------------------
# orderBy() → sorting
# --------------------------------
df.orderBy(df.Collection.desc()).show()

# Sorts data in descending order
# Like SQL: ORDER BY Collection DESC


# --------------------------------
# groupBy() → grouping + aggregation
# --------------------------------
from pyspark.sql.functions import avg

df.groupBy("Genre").avg("Collection").show()

# groupBy → divides rows into groups
# avg → aggregation function
# Like SQL: GROUP BY


# --------------------------------
# withColumnRenamed() → rename column
# --------------------------------
df = df.withColumnRenamed("Collection", "BoxOffice")

# DataFrames are IMMUTABLE → new DataFrame created
# Old column name replaced


# --------------------------------
# withColumn() → create new column
# --------------------------------
df = df.withColumn("PerformanceScore", df.BoxOffice * df.Rating)

# Column-to-column operation
# Applied row-wise


# --------------------------------
# lit() → constant value
# --------------------------------
from pyspark.sql.functions import lit

df = df.withColumn("Industry", lit("Film"))

# lit() = literal value
# Required because Spark expects COLUMN, not raw value
# df.withColumn("Industry", "Film") → ❌ ERROR


# --------------------------------
# when() otherwise() → condition (IF-ELSE)
# --------------------------------
from pyspark.sql.functions import when

df = df.withColumn(
    "HitStatus",
    when((df.BoxOffice > 1000) & (df.Rating > 7), "Hit")
    .when(df.BoxOffice > 500, "Average")
    .otherwise("Flop")
)

# WHY NOT if-else?
# Because:
# DataFrame = distributed (multiple machines)
# if-else = works on single value
# So Spark uses when() for parallel condition execution

# when → IF
# .when → ELSE IF
# otherwise → ELSE


# ==============================
# FINAL OUTPUT
# ==============================

df.show()


# ==============================
# 🔥 IMPORTANT EXAM POINTS
# ==============================

# 1. Spark uses LAZY EVALUATION
#    → execution only when action (show, count)

# 2. DataFrames are IMMUTABLE
#    → every operation returns new DataFrame

# 3. lit() is required for constants

# 4. when() replaces if-else in distributed systems

# 5. groupBy() must use aggregation (avg, sum, count)


# ==============================
# END
# ==============================
'''