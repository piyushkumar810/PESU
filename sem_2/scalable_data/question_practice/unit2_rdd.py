# Question 1 (8 Marks) – sc.parallelize()
'''
Create an RDD using:
[10, 15, 20, 25, 30, 35, 40]

Perform the following operations:

1.Display all elements.
2.Count the number of elements.
3.Display only numbers greater than 20.
4.Multiply every element by 5.
5.Find the sum of all elements.
'''

# solution
'''roll = [10, 15, 20, 25, 30, 35, 40]

rdd = sc.parallelize(roll)

# Display all elements
rdd.collect()

# Count elements
total_std = rdd.count()       #because count return integer not rdd so used print
print(total_std)

# Filter numbers greater than 20
rdd1 = rdd.filter(lambda x: x > 20)
rdd1.collect()

# Multiply each element by 5
rdd2 = rdd.map(lambda x: x * 5)
rdd2.collect()

# Find sum
total = rdd.reduce(lambda x, y: x + y)    # sum also return integer not rdd
print(total)
'''




# Q2)
'''
Read a text file named data.txt using sc.textFile().

Perform the following:

Display the contents of the file.
Count the total number of lines.
Display the first line.
Display the first three lines.
Filter and display only the lines containing the word Spark.
'''

# solution
'''
rdd = sc.textFile("data.txt")

# Display all lines
rdd.collect()

# Count total lines
print(rdd.count())

# Display first line
print(rdd.first())

# Display first three lines
print(rdd.take(3))

# Display lines containing "Spark"
rdd.filter(lambda x: "Spark" in x).collect()
'''


# Q3)
'''
Q. Read sales.txt using sc.textFile() and perform the following:

#----------- dataset
Laptop,2
Mobile,3
Laptop,4
Tablet,1
Mobile,2
Laptop,5
Tablet,3

1.Read the file.
2.Display all records.
3.Convert the data into a Key-Value RDD.
4.Display the Key-Value pairs.
5.Use reduceByKey() to calculate the total quantity sold for each product.
6.Display the final result.
'''

# solution
'''
# Read file
rdd = sc.textFile("sales.txt")

# Display all records
print(rdd.collect())

# Convert to Key-Value RDD
kv = rdd.map(lambda x: (x.split(",")[0], int(x.split(",")[1])))

# Display Key-Value pairs
print(kv.collect())

# Apply reduceByKey()
result = kv.reduceByKey(lambda x, y: x + y)

# Display final result
print(result.collect())
'''