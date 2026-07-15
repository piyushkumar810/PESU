# from pyspark.sql import SparkSession
# from pyspark.sql.functions import avg

# # Create Spark Session
# spark = SparkSession.builder.appName("Student").getOrCreate()

# # Read CSV File
# df = spark.read.csv("student.csv", header=True, inferSchema=True)

# # Display Data
# df.show()

# # Filter Students with Marks > 80
# filtered = df.filter(df.Marks > 80)

# filtered.show()

# # Group By Department
# group = df.groupBy("Department").count()

# group.show()

# # Average Marks
# average = df.groupBy("Department").agg(avg("Marks"))

# average.show()