'''
1. Open Command Prompt (Windows)

   C:\Users\piyush kumar>

------------------------------------------------------------

2. Open WSL Ubuntu Environment

   Command:
   wsl -d bigdata-env

------------------------------------------------------------

3. Switch to Hadoop User

   Command:
   su hadoop

------------------------------------------------------------

4. Go to /opt Directory

   Command:
   cd /opt

------------------------------------------------------------

5. Check Installed Big Data Tools

   Command:
   ls

   Output:
   cassandra
   containerd
   flink-1.20.0
   hadoop-3.4.0
   kafka
   pig-0.17.0
   spark-3.5.5-bin-hadoop3-scala2.13

------------------------------------------------------------

6. Move to Flink Folder

   Command:
   cd flink-1.20.0

------------------------------------------------------------

7. Check Flink Directory Contents

   Command:
   ls

   Output:
   LICENSE
   NOTICE
   README.txt
   bin
   conf
   examples
   lib
   licenses
   log
   opt
   plugins
   programs

------------------------------------------------------------

8. Move to Flink bin Folder

   Command:
   cd bin

------------------------------------------------------------

9. Check Available Flink Scripts

   Command:
   ls

   Important Files:
   flink
   start-cluster.sh
   stop-cluster.sh
   taskmanager.sh
   jobmanager.sh
   pyflink-shell.sh

------------------------------------------------------------

10. Start Flink Cluster

   Command:
   ./start-cluster.sh

   Output:
   Starting cluster.
   Starting standalonesession daemon on host piyush-laptop.
   Starting taskexecutor daemon on host piyush-laptop.

------------------------------------------------------------

11. Verify Flink Services using JPS

   Command:
   jps

   Output:
   1634 StandaloneSessionClusterEntrypoint
   2188 TaskManagerRunner
   2312 Jps

   Meaning:
   ✔ JobManager Running
   ✔ TaskManager Running

------------------------------------------------------------

12. Go Back to Flink Main Folder

   Command:
   cd ..

------------------------------------------------------------

13. Move to programs Folder

   Command:
   cd programs

------------------------------------------------------------

14. Create Python Program File

   Command:
   nano celsius.py

------------------------------------------------------------

15. Write PyFlink Program inside celsius.py

   Example Program:

   
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.typeinfo import Types


def celsius_to_fahrenheit(record):
    city, celsius = record
    fahrenheit = (celsius * 9 / 5) + 32
    return city, celsius, round(fahrenheit, 2)


env = StreamExecutionEnvironment.get_execution_environment()

ds = env.from_collection(
    [
        ("Bengaluru", 26),
        ("Delhi", 34),
        ("Mumbai", 30),
        ("Chennai", 32)
    ],
    type_info=Types.TUPLE([Types.STRING(), Types.INT()])
)

result = ds.map(
    celsius_to_fahrenheit,
    output_type=Types.TUPLE(
        [Types.STRING(), Types.INT(), Types.FLOAT()]
    )
)

result.print()

env.execute("map-celsius-to-fahrenheit")
   
'''

'''
------------------------------------------------------------

16. Save and Exit nano Editor

   Press:
   CTRL + O  → Save
   ENTER     → Confirm
   CTRL + X  → Exit

------------------------------------------------------------

17. Go Back to bin Folder

   Command:
   cd ../bin

------------------------------------------------------------

18. Run PyFlink Program

   Command:
   ./flink run -py ../programs/celsius.py

------------------------------------------------------------

19. Output After Execution

   Output:
   Job has been submitted with JobID xxxxxxxxx

   Program execution finished

   Job with JobID xxxxxxxxx has finished.

   Job Runtime: 6175 ms

------------------------------------------------------------


# ------------------------- output you will get in chrome :- 
# 1st go:- localhose:8081
# 2nd:- overview
# 3rd:- completed job list
# 4th:- job manager log
# 5th:- log list
# 6th:- tap twice last modified time
# 7th:- check 1st .out file -> there you will get output
'''





'''
20. Flow Summary

   Windows CMD
        ↓
   WSL Ubuntu
        ↓
   Hadoop User
        ↓
   /opt/flink-1.20.0
        ↓
   Start Cluster
        ↓
   Verify using jps
        ↓
   Create Python File
        ↓
   Write PyFlink Code
        ↓
   Run using flink run -py
        ↓
   Job Executed Successfully

------------------------------------------------------------

21. Important Commands Quick Revision

   Start Cluster:
   ./start-cluster.sh

   Stop Cluster:
   ./stop-cluster.sh

   Check Java Processes:
   jps

   Run PyFlink Program:
   ./flink run -py filename.py

------------------------------------------------------------
22. Common Mistakes You Did

   ❌ cd /flink-1.20.0
   ✔ Correct:
      cd /opt/flink-1.20.0

   ❌ ./start - cluster.sh
   ✔ Correct:
      ./start-cluster.sh

   ❌ c dbin
   ✔ Correct:
      cd bin
'''