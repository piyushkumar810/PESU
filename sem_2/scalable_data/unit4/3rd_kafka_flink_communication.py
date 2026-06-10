'''EL VII : KAFKA ↔ FLINK COMPLETE LAB FLOW

STEP 0 : START FLINK

Terminal 0

cd /opt/flink-1.20.0/bin

./start-cluster.sh

Verify:

jps

Output:

JobManager
TaskManager

---

STEP 1 : START KAFKA SERVER

Terminal 1

cd /opt/kafka

bin/kafka-server-start.sh 
config/kraft/server.properties

Keep Terminal 1 OPEN

---

STEP 2 : CREATE TOPICS

Terminal 2

cd /opt/kafka

Create Input Topic

bin/kafka-topics.sh 
--bootstrap-server localhost:9092 
--create 
--topic flink-input 
--partitions 1 
--replication-factor 1

Create Output Topic

bin/kafka-topics.sh 
--bootstrap-server localhost:9092 
--create 
--topic flink-output 
--partitions 1 
--replication-factor 1

Verify Topics

bin/kafka-topics.sh 
--bootstrap-server localhost:9092 
--list

Output:

flink-input
flink-output

---

STEP 3 : START PRODUCER

Terminal 3

cd /opt/kafka

bin/kafka-console-producer.sh 
--bootstrap-server localhost:9092 
--topic flink-input

Now type:

hello
flink
kafka

Keep Terminal 3 OPEN

---

STEP 4 : START CONSUMER

Terminal 4

cd /opt/kafka

bin/kafka-console-consumer.sh 
--bootstrap-server localhost:9092 
--topic flink-input 
--from-beginning

Output:

hello
flink
kafka

Keep Terminal 4 OPEN

---

STEP 5 : CREATE PYFLINK PROJECT

Terminal 5

cd ~

mkdir kafka-flink

cd kafka-flink

---

STEP 6 : CREATE PYTHON FILE

Terminal 5

nano kafka_flink.py

Paste code below

---

PROGRAM 1
KAFKA SOURCE → FLINK

from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors.kafka import FlinkKafkaConsumer
from pyflink.common.serialization import SimpleStringSchema

env = StreamExecutionEnvironment.get_execution_environment()

consumer = FlinkKafkaConsumer(
'flink-input',
SimpleStringSchema(),
{
'bootstrap.servers':'localhost:9092',
'group.id':'flink-demo'
}
)

consumer.set_start_from_earliest()

ds = env.add_source(consumer)

ds.print()

env.execute("Kafka Source Demo")

---

SAVE FILE

CTRL + X

Y

ENTER

---

RUN PROGRAM

python3 kafka_flink.py

Output:

hello
flink
kafka

---

PROGRAM 2
MAP TRANSFORMATION

Replace:

ds.print()

With:

result = ds.map(lambda x:x.upper())

result.print()

Run:

python3 kafka_flink.py

Producer Input:

hello
flink
kafka

Output:

HELLO
FLINK
KAFKA

---

PROGRAM 3
FILTER TRANSFORMATION

Replace:

result = ds.map(lambda x:x.upper())

With:

result = ds.filter(
lambda x: len(x)>5
)

result.print()

Input:

hi
hello
flink
kafka

Output:

hello

Only strings length > 5 printed

---

PROGRAM 4
KAFKA → FLINK → KAFKA

from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors.kafka import (
FlinkKafkaConsumer,
FlinkKafkaProducer
)
from pyflink.common.serialization import SimpleStringSchema

env = StreamExecutionEnvironment.get_execution_environment()

consumer = FlinkKafkaConsumer(
"flink-input",
SimpleStringSchema(),
{
"bootstrap.servers":"localhost:9092",
"group.id":"flink-demo"
}
)

producer = FlinkKafkaProducer(
topic="flink-output",
serialization_schema=SimpleStringSchema(),
producer_config={
"bootstrap.servers":"localhost:9092"
}
)

ds = env.add_source(consumer)

result = ds.map(lambda x:x.upper())

result.add_sink(producer)

env.execute("Kafka To Kafka")

---

RUN

python3 kafka_flink.py

---

STEP 7 : VIEW OUTPUT TOPIC

Terminal 6

cd /opt/kafka

bin/kafka-console-consumer.sh 
--bootstrap-server localhost:9092 
--topic flink-output 
--from-beginning

Producer Input:

hello
flink
kafka

Output Topic:

HELLO
FLINK
KAFKA

---

FINAL FLOW

Terminal 1
Kafka Server

↓

Terminal 3
Producer

↓

Topic : flink-input

↓

Terminal 5
PyFlink Program

↓

map/filter

↓

Topic : flink-output

↓

Terminal 6
Consumer

---

EXAM FLOW

Start Flink
↓
Start Kafka
↓
Create Topics
↓
Start Producer
↓
Start Consumer
↓
Create Python File
↓
Write PyFlink Code
↓
Run python3 kafka_flink.py
↓
Observe Output
'''