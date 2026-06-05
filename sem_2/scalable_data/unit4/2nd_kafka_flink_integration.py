'''KAFKA + FLINK INTEGRATION (TOPIC TO TOPIC DATA TRANSFER)

Objective:
To read messages from Kafka topic "newtopic1" using PyFlink, process the data, and write the result to another Kafka topic "newtopic".

────────────────────────────────────────
TERMINAL 1 : KAFKA SETUP + PRODUCER
────────────────────────────────────────

Step 1: Open WSL and switch to Hadoop user

Command:
wsl -d bigdata-env
su hadoop

Purpose:
Login into the Linux environment where Kafka is installed.

---

Step 2: Move to Kafka directory

Command:
cd /opt/kafka

Purpose:
Navigate to Kafka installation folder.

---

Step 3: Start ZooKeeper

Command:
./bin/zookeeper-server-start.sh -daemon config/zookeeper.properties

Purpose:
ZooKeeper manages Kafka brokers and cluster metadata.

---

Step 4: Verify ZooKeeper is running

Command:
jps

Output:
QuorumPeerMain

Purpose:
Confirms ZooKeeper started successfully.

---

Step 5: Start Kafka Broker

Command:
./bin/kafka-server-start.sh -daemon config/server.properties

Purpose:
Starts Kafka server to handle producers and consumers.

---

Step 6: Verify Kafka is running

Command:
jps

Output:
Kafka
QuorumPeerMain

Purpose:
Confirms Kafka Broker is active.

---

Step 7: List existing topics

Command:
./bin/kafka-topics.sh --list --bootstrap-server localhost:9092

Purpose:
Shows all available Kafka topics.

---

Step 8: Create Input Topic

Command:
./bin/kafka-topics.sh --create --topic newtopic1 --bootstrap-server localhost:9092

Purpose:
Creates topic where producer sends messages.

---

Step 9: Create Output Topic

Command:
./bin/kafka-topics.sh --create --topic newtopic --bootstrap-server localhost:9092

Purpose:
Creates topic where Flink writes processed data.

---

Step 10: Verify Topics

Command:
./bin/kafka-topics.sh --list --bootstrap-server localhost:9092

Output:
newtopic
newtopic1

Purpose:
Confirms topics were created successfully.

---

Step 11: Start Producer

Command:
./bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic newtopic1

Purpose:
Send messages to input topic.

Example:
hello
flink
kafka

────────────────────────────────────────
TERMINAL 2 : KAFKA CONSUMER
────────────────────────────────────────

Step 1: Open WSL and switch to Hadoop user

Command:
wsl -d bigdata-env
su hadoop

Purpose:
Access Kafka environment.

---

Step 2: Go to Kafka directory

Command:
cd /opt/kafka

Purpose:
Navigate to Kafka installation.

---

Step 3: Verify services

Command:
jps

Expected:
Kafka
QuorumPeerMain
ConsoleProducer

Purpose:
Ensures Kafka and Producer are running.

---

Step 4: Start Consumer

Command:
./bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic newtopic

Purpose:
Reads processed messages from output topic.

Expected:
HELLO
FLINK
KAFKA

(after Flink job starts successfully)

────────────────────────────────────────
TERMINAL 3 : FLINK CLUSTER + PYFLINK JOB
────────────────────────────────────────

Step 1: Open WSL and switch to Hadoop user

Command:
wsl -d bigdata-env
su hadoop

Purpose:
Access Flink environment.

---

Step 2: Move to Flink directory

Command:
cd /opt/flink-1.20.0/bin

Purpose:
Navigate to Flink executable directory.

---

Step 3: Start Flink Cluster

Command:
./start-cluster.sh

Purpose:
Starts JobManager and TaskManager.

---

Step 4: Verify Cluster

Command:
jps

Expected:
StandaloneSessionClusterEntrypoint
TaskManagerRunner

Purpose:
Confirms Flink cluster is running.

---

Step 5: Edit PyFlink Program

Command:
nano ../programs/upper_kafka_flink.py

Purpose:
Write Kafka-Flink integration code.

Processing Logic:

1. Read messages from topic "newtopic1"
2. Convert text to uppercase
3. Write result to topic "newtopic"

---

Step 6: Run Flink Job

Command:
./flink run -py ../programs/upper_kafka_flink.py

Purpose:
Submits PyFlink job to cluster.

────────────────────────────────────────
DATA FLOW
────────────────────────────────────────

Producer
│
▼
Kafka Topic : newtopic1
│
▼
PyFlink Job
(Convert text to UPPERCASE)
│
▼
Kafka Topic : newtopic
│
▼
Consumer

Example:

Producer Input:
hello
kafka
flink

Flink Processing:
hello → HELLO
kafka → KAFKA
flink → FLINK

Consumer Output:
HELLO
KAFKA
FLINK

────────────────────────────────────────
CURRENT STATUS
────────────────────────────────────────

✓ ZooKeeper Running
✓ Kafka Running
✓ Producer Running
✓ Consumer Running
✓ Flink Cluster Running
✓ Topics Created
✓ PyFlink Program Created

Current Issue:
Kafka Connector Dependency Error

Error:
java.lang.NoClassDefFoundError:
org/apache/kafka/common/serialization/ByteArrayDeserializer

Reason:
Kafka client libraries/connector dependencies are not properly available to Flink.
'''