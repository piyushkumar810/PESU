'''
Kafka Architecture

                 +------------------+
                 |   ZooKeeper      |
                 |  Port : 2181     |
                 +--------+---------+
                          |
                          |
                 +--------v---------+
                 |   Kafka Broker   |
                 |  Port : 9092     |
                 +--------+---------+
                          |
            ------------------------------
            |                            |
            |                            |
    +-------v-------+            +-------v-------+
    |   Producer    |            |   Consumer    |
    +---------------+            +---------------+
            |                            ^
            |                            |
            +-------- Topic ------------+
                     newtopic1
'''

'''
KAFKA PRODUCER-CONSUMER FLOW
│
├── Step 1 : Open WSL
│   │
│   ├── Command
│   │   └── wsl -d bigdata-env
│   │
│   └── Switch User
│       └── su hadoop
│
├── Step 2 : Go to Kafka Directory
│   │
│   └── cd /opt/kafka
│
├── Step 3 : Start ZooKeeper
│   │
│   └── ./bin/zookeeper-server-start.sh -daemon config/zookeeper.properties
│
│       ZooKeeper
│       │
│       ├── Stores Kafka Metadata
│       ├── Broker Information
│       ├── Leader Election
│       └── Configuration Management
│
├── Step 4 : Verify ZooKeeper
│   │
│   └── jps
│       │
│       └── QuorumPeerMain
│            │
│            └── ZooKeeper Running
│
├── Step 5 : Start Kafka Broker
│   │
│   └── ./bin/kafka-server-start.sh -daemon config/server.properties
│
│       Kafka Broker
│       │
│       ├── Receives Messages
│       ├── Stores Messages
│       └── Serves Consumers
│
├── Step 6 : Verify Kafka
│   │
│   └── jps
│       │
│       ├── Kafka
│       │    └── Broker Running
│       │
│       └── QuorumPeerMain
│            └── ZooKeeper Running
│
├── Step 7 : Create Topic
│   │
│   └── ./bin/kafka-topics.sh --create --topic newtopic --bootstrap-server localhost:9092
│
│       Kafka Broker
│       │
│       └── Topic : newtopic
│
│           Topic
│           │
│           ├── Message 1
│           ├── Message 2
│           └── Message 3
│
├── Step 8 : Start Producer
│   │
│   └── ./bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic newtopic1
│
│       Producer
│       │
│       ├── piyush
│       ├── priyanshu
│       └── rohit
│
│               │
│               ▼
│
│          Topic : newtopic1
│
├── Step 9 : Verify Producer
│   │
│   └── jps
│       │
│       └── ConsoleProducer
│            │
│            └── Producer Running
│
├── Step 10 : Open Consumer Terminal
│   │
│   ├── wsl -d bigdata-env
│   ├── su hadoop
│   └── cd /opt/kafka
│
├── Step 11 : Verify Services
│   │
│   └── jps
│       │
│       ├── Kafka
│       ├── QuorumPeerMain
│       └── ConsoleProducer
│
├── Step 12 : Start Consumer
│   │
│   └── ./bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic newtopic1
│
│       Consumer
│       │
│       └── Reads Messages From Topic
│
├── Step 13 : LEADER_NOT_AVAILABLE Warning
│   │
│   ├── Topic Created
│   │
│   ├── Leader Election Starts
│   │
│   ├── Consumer Requests Metadata
│   │
│   └── Temporary Warning Appears
│
│       (Not an Error)
│
└── Step 14 : Message Flow
    │
    ├── Producer
    │    ├── piyush
    │    ├── priyanshu
    │    └── rohit
    │
    ▼
    Topic : newtopic1
    │
    ▼
    Kafka Broker
    │
    ▼
    Consumer
    │
    ├── piyush
    ├── priyanshu
    └── rohit
'''


# final architecture
'''
                    ZooKeeper
                         │
                         ▼
                 +---------------+
                 | Kafka Broker  |
                 +-------+-------+
                         │
                         ▼
                   Topic:newtopic1
                         │
            ┌────────────┴────────────┐
            │                         │
            ▼                         ▼

      +-----------+             +-----------+
      | Producer  |             | Consumer  |
      +-----------+             +-----------+
            │
            ├── piyush
            ├── priyanshu
            └── rohit
'''



# interview question
'''
Producer sends messages to a Kafka Topic.
Kafka Broker stores those messages.
Consumer reads messages from the Topic.
ZooKeeper manages Kafka metadata, broker information,
and leader election.
'''