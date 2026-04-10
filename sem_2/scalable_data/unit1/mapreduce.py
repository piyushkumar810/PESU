'''
START (Windows CMD)
│
├── Step 1: Open WSL (Linux Environment)
│   └── wsl -d bigdata-env
│       # Opens Hadoop environment
│
├── Step 2: Switch to Hadoop User
│   └── su - hadoop
│       # Required permissions to run Hadoop
│
├── Step 3: Start Hadoop Services
│   ├── start-dfs.sh
│   │   # Starts HDFS (NameNode + DataNode)
│   │
│   ├── start-yarn.sh
│   │   # Starts YARN (ResourceManager + NodeManager)
│   │
│   └── jps
│       # Verify services are running
│       # Expected:
│       # NameNode, DataNode, SecondaryNameNode, ResourceManager, NodeManager
│
├── Step 4: Create Input File (LOCAL SYSTEM)
│   ├── echo "hello world hello hadoop world" > input.txt
│   │   # Creates file in local Linux (NOT HDFS)
│   │
│   └── ls
│       # Verify file exists
│
├── Step 5: Create Directory in HDFS
│   ├── hdfs dfs -mkdir /input
│   │   # Metadata operation (NameNode only)
│   │
│   └── hdfs dfs -ls /
│       # Verify directory
│
├── Step 6: Upload File to HDFS
│   ├── hdfs dfs -put input.txt /input
│   │   # File split into blocks + stored in DataNodes + replication
│   │
│   └── hdfs dfs -ls /input
│       # Verify upload
│
├── Step 7: Read File from HDFS (Optional)
│   └── hdfs dfs -cat /input/input.txt
│       # Data read from DataNodes
│
├── Step 8: Create MapReduce Code (LOCAL)
│   │
│   ├── Create Mapper
│   │   ├── nano mapper.py
│   │   │   # Open editor
│   │   │
│   │   ├── Paste Python code
│   │   │   # Emits (word,1)
│   │   │
│   │   └── Save → CTRL+X → Y → Enter
│   │
│   ├── Create Reducer
│   │   ├── nano reducer.py
│   │   │
│   │   ├── Paste Python code
│   │   │   # Aggregates counts
│   │   │
│   │   └── Save → CTRL+X → Y → Enter
│   │
│   └── chmod +x mapper.py reducer.py
│       # Make scripts executable
│
├── Step 9: Run MapReduce Job
│   ├── hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming*.jar \
│   │   -input /input \
│   │   -output /output \
│   │   -mapper mapper.py \
│   │   -reducer reducer.py
│   │
│   │   # FULL FLOW:
│   │   # HDFS → Input Split → Mapper → Shuffle → Reducer → HDFS
│   │
│   └── (If error: output exists)
│       └── hdfs dfs -rm -r /output
│           # Delete old output
│
├── Step 10: View Output
│   └── hdfs dfs -cat /output/part-00000
│       # Final result from reducer
│
└── END
'''