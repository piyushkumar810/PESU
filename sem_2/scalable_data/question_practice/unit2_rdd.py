'''
Question 1 (8 Marks) – sc.parallelize()
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