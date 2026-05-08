'''Windows CMD
│
├── Open WSL Ubuntu
│   └── wsl -d bigdata-env
│
├── Switch user
│   └── su - hadoop
│
├── Go to Flink Folder
│   └── cd /opt/flink-1.20.0
│
├── Start Flink Cluster
│   │
│   ├── cd bin
│   └── ./start-cluster.sh
│
├── Go to Programs Folder
│   │
│   ├── cd ..
│   └── cd programs
│
├── Create Python File
│   └── nano student_stream.py
│
├── Write Code
│
├── Save File
│   │
│   ├── Ctrl + O
│   ├── Enter
│   └── Ctrl + X
│
├── Run Program
│   │
│   ├── cd ..
│   ├── cd bin
│   └── ./flink run -py /opt/flink-1.20.0/programs/student_stream.py
│
└── Output Generated'''
'''

from pyflink.datastream import StreamExecutionEnvironment

# Create Flink execution environment
env = StreamExecutionEnvironment.get_execution_environment()

# Input data as list of tuples
# Format: (Student Name, Department)
students = [
    ("Alice", "CS"),
    ("Bob", "IT"),
    ("Charlie", "CS"),
    ("David", "ECE")
]

# Convert Python list into Flink DataStream
ds = env.from_collection(students)

# MAP Transformation
# Converts student names into uppercase
# x[0] -> student name
# x[1] -> department
mapped_ds = ds.map(lambda x: (x[0].upper(), x[1]))

# FLAT_MAP Transformation
# Splits department name into separate characters
# Example:
# ("ALICE","CS") -> ("ALICE","C"), ("ALICE","S")
flatmapped_ds = mapped_ds.flat_map(
    lambda x: [(x[0], ch) for ch in x[1]]
)

# FILTER Transformation
# Keeps only records where second value is "C"
filtered_ds = flatmapped_ds.filter(lambda x: x[1] == "C")

# KEY_BY Transformation
# Groups records using student name as key
keyed_ds = filtered_ds.key_by(lambda x: x[0])

# Print final output
keyed_ds.print()

# Execute Flink program
env.execute("PyFlink Transformation Example")'''