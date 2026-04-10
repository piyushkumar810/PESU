'''🚀 PART 1: Starting Environment

✅ 1. Start WSL
wsl -d bigdata-env

👉 Opens your Linux environment (Ubuntu inside Windows)

✅ 2. Switch User
su - hadoop

👉 You logged in as hadoop user
Why? Because Hadoop/Spark usually run under a specific user.


🚀 PART 2: Start PySpark

✅ 3. Start Spark
pyspark
👉 This does:

Starts Spark Engine
Creates:
sc → SparkContext
spark → SparkSession

💡 VERY IMPORTANT:

sc → used for RDD
spark → used for DataFrames
'''

# PYSPARK COMPLETE COMMAND TREE
'''
PySpark
│
├── 1. Spark Entry Points
│
├── 2. RDD Creation
│
├── 3. Transformations (Lazy)
│
├── 4. Actions (Execution)
│
├── 5. Partition Operations
│
├── 6. Pair RDD Operations
│
├── 7. Shared Variables
│
└── 8. Advanced Concepts
'''

'''
PYSPARK COMPLETE TREE (WITH COMMENTS)

# ==============================

# 🌳 PYSPARK STRUCTURE

# ==============================

PySpark
│
├── 1. Spark Entry Points
│   ├── sc (SparkContext)
│   │   # Used for RDD operations (low-level API)
│   │   # Example:
│   │   # rdd = sc.parallelize([1,2,3])
│   │
│   └── spark (SparkSession)
│       # Used for DataFrames & SQL
│       # Example:
│       # df = spark.read.csv("file.csv")
│
├── 2. RDD Creation
│   ├── parallelize()
│   │   # Converts Python list → RDD
│   │   # rdd = sc.parallelize([1,2,3])
│   │
│   ├── textFile()
│   │   # Reads file → each line is one element
│   │   # rdd = sc.textFile("file.txt")
│   │
│   └── wholeTextFiles()
│       # Reads multiple files → (filename, content)
│       # rdd = sc.wholeTextFiles("folder/")
│
├── 3. Transformations (LAZY ⚡)
│   # These DO NOT execute immediately
│   # Execution happens only after ACTION
│   │
│   ├── map()
│   │   # 1 input → 1 output
│   │   # rdd.map(lambda x: x+1)
│   │
│   ├── flatMap()  🔥 IMPORTANT
│   │   # 1 input → multiple outputs
│   │   # rdd.flatMap(lambda x: x.split())
│   │
│   ├── filter()
│   │   # Keeps elements that satisfy condition
│   │   # rdd.filter(lambda x: x%2==0)
│   │
│   ├── distinct()
│   │   # Removes duplicates
│   │
│   ├── union()
│   │   # Combines two RDDs
│   │
│   ├── intersection()
│   │   # Common elements
│   │
│   ├── subtract()
│   │   # Removes elements of second RDD
│   │
│   ├── cartesian()
│   │   # All possible pairs (VERY EXPENSIVE ⚠️)
│   │
│   └── sample()
│       # Random sampling of data
│
├── 4. Actions (EXECUTION 🔴)
│   # These TRIGGER execution
│   │
│   ├── collect()
│   │   # Brings all data to local machine ⚠️ (danger for big data)
│   │
│   ├── count()
│   │   # Returns total number of elements
│   │
│   ├── first()
│   │   # Returns first element
│   │
│   ├── take(n)
│   │   # Returns first n elements
│   │
│   ├── reduce()
│   │   # Aggregates data
│   │   # rdd.reduce(lambda a,b: a+b)
│   │
│   ├── foreach()
│   │   # Applies function (distributed)
│   │
│   ├── saveAsTextFile()
│   │   # Saves RDD to file
│   │
│   └── countByValue()
│       # Frequency of each element
│
├── 5. Partition Operations 🔥
│   │
│   ├── getNumPartitions()
│   │   # Returns number of partitions
│   │
│   ├── repartition(n)
│   │   # Changes partitions (SHUFFLE ⚠️ expensive)
│   │   # Used to increase/decrease partitions
│   │
│   ├── coalesce(n)
│   │   # Reduces partitions (NO shuffle → efficient)
│   │
│   └── mapPartitions() 🔥 IMPORTANT
│       # Works on entire partition instead of single element
│
├── 6. Pair RDD Operations 🔥🔥
│   # Works on (key, value) pairs
│   │
│   ├── reduceByKey()  🔥 MOST IMPORTANT
│   │   # Aggregates values by key (efficient)
│   │
│   ├── groupByKey()
│   │   # Groups values (inefficient ⚠️)
│   │
│   ├── sortByKey()
│   │   # Sorts by key
│   │
│   ├── keys()
│   │   # Extracts keys
│   │
│   ├── values()
│   │   # Extracts values
│   │
│   └── join()
│       # Joins two RDDs (like SQL JOIN)
│
├── 7. Shared Variables
│   │
│   ├── Broadcast
│   │   # Read-only shared variable across nodes
│   │   # bc = sc.broadcast(data)
│   │
│   └── Accumulator
│       # Used for counting/summing across workers
│       # acc = sc.accumulator(0)
│
└── 8. Advanced Concepts 🔥
│
├── Lazy Evaluation
│   # Transformations are NOT executed immediately
│
├── DAG (Directed Acyclic Graph)
│   # Execution plan of Spark
│
├── Shuffle ⚠️
│   # Data movement across partitions (costly)
│
└── Persistence (cache)
# Stores data in memory for reuse
# rdd.cache()

# ==============================

# 🚀 FULL FLOW (REMEMBER)

# ==============================

# Data → RDD → Transformations → Action → Execution → Result

# ==============================

# 🔥 VERY IMPORTANT POINTS

# ==============================

# ✔ Transformations = Lazy

# ✔ Actions = Execute

# ✔ RDD is NOT iterable

# ✔ RDD is NOT indexable

# ✔ repartition = shuffle (costly)

# ✔ reduceByKey > groupByKey (efficient)

'''

