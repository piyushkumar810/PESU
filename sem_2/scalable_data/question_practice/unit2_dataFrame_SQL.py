# Q) complete DataFrame + Spark SQL
'''
Read student.csv using spark.read.csv() and perform the following:

# ----------------dataset-----------------
Name,Age,Marks,Department
Piyush,22,85,MCA
Rahul,21,78,MCA
Ankit,23,90,MBA
Sneha,22,88,MCA
Priya,24,76,MBA


1.Read the CSV file.
2.Display all records.
3.Print the schema.
4.Display only the Name and Marks columns.
5.Display students whose marks are greater than 80.
6.Create a temporary SQL view.
7.Use Spark SQL to display students from the MCA department.
8.Count the total number of students.
'''

# solution
'''
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Example").getOrCreate()
sc = spark.sparkContext

# Read CSV
df = spark.read.csv("student.csv", header=True, inferSchema=True)

# Display records
df.show()

# Print schema
df.printSchema()

# Display Name and Marks
df.select("Name", "Marks").show()

# Students with Marks > 80
df.filter(df.Marks > 80).show()

# Create SQL View
df.createOrReplaceTempView("students")

# SQL Query
spark.sql("SELECT * FROM students WHERE Department='MCA'").show()

# Count students
print(df.count())

'''