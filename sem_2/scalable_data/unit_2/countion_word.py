
'''
# ================================
# STEP 0: (Outside PySpark - Terminal)
# ================================
# Create file using nano (Linux command, NOT Python)
# nano data.txt
# → Write paragraph → Save (CTRL+X → Y → ENTER)

# ================================
# STEP 1: Start PySpark (Terminal)
# ================================
# pyspark

# ================================
# STEP 2: Load File into RDD
# ================================
file = sc.textFile("data.txt")
# sc → SparkContext
# textFile() → loads file as RDD (each line = one element)

# ================================
# STEP 3: Check File Content
# ================================
file.collect()
# collect() → brings ALL data from cluster to screen (driver)
# Used for checking whether file loaded correctly

# ================================
# STEP 4: Split Lines into Words
# ================================
words = file.flatMap(lambda line: line.split())
# flatMap() → one line → multiple words
# split() → splits sentence into words

words.take(10)
# take(10) → shows first 10 words (safe checking)

# ================================
# STEP 5: Convert Words to Key-Value Pair
# ================================
kvp = words.map(lambda word: (word, 1))
# map() → transforms each word into (word,1)
# Example: "data" → ("data",1)

kvp.take(5)
# check first 5 pairs

# ================================
# STEP 6: Count Words (IMPORTANT STEP)
# ================================
wordcount = kvp.reduceByKey(lambda a, b: a + b)
# reduceByKey() → combines values of same key
# Example: ("data",1) + ("data",1) → ("data",2)

# ================================
# STEP 7: Display Final Result
# ================================
wordcount.collect()
# Final output: [('data',3), ('hadoop',2), ...]

# ================================
# (OPTIONAL - CLEAN DATA)
# ================================
import re
words = file.flatMap(lambda line: re.findall(r'\w+', line.lower()))
# Removes punctuation and converts to lowercase
# Better and cleaner output

'''


'''
🔥 LAST-MINUTE VIVA POINTS
-------------------------------------
RDD → Distributed data collection
flatMap() → 1 → many
map() → transform data
reduceByKey() → aggregation
collect() → bring all data to driver
take(n) → safe preview
'''