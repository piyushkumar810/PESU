'''
Topic
PyFlink Sliding Event Time Window

This program demonstrates:

Event Time Processing
Watermark Strategy
Timestamp Assignment
Sliding Event Time Windows
Stream Processing using PyFlink
Real-time Sales Aggregation
Full Complete Code'''

from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.watermark_strategy import (
    WatermarkStrategy,
    TimestampAssigner
)

from pyflink.datastream.window import SlidingEventTimeWindows
from pyflink.datastream.functions import ReduceFunction

from pyflink.common import Time
from pyflink.common.typeinfo import Types


# ---------------------------------------------------------
# Step 1: Create Stream Execution Environment
# ---------------------------------------------------------

env = StreamExecutionEnvironment.get_execution_environment()

# Set parallelism = 1
# So output comes in sequence
env.set_parallelism(1)


# ---------------------------------------------------------
# Step 2: Input Data
#
# Format:
# (timestamp, shop_name, sales_amount)
#
# Timestamp is in milliseconds
# ---------------------------------------------------------

data = [
    (5000,  "shop1", 100),
    (7000,  "shop1", 200),
    (12000, "shop1", 150),
    (15000, "shop1", 300),
    (22000, "shop1", 250)
]


# ---------------------------------------------------------
# Step 3: Create Data Stream
# ---------------------------------------------------------

ds = env.from_collection(
    collection=data,

    type_info=Types.TUPLE([
        Types.LONG(),    # timestamp
        Types.STRING(),  # shop name
        Types.INT()      # sales amount
    ])
)


# ---------------------------------------------------------
# Step 4: Create Timestamp Assigner
#
# Extract timestamp from each record
# ---------------------------------------------------------

class MyTimestampAssigner(TimestampAssigner):

    def extract_timestamp(self, value, record_timestamp):

        # value[0] contains timestamp
        return value[0]


# ---------------------------------------------------------
# Step 5: Watermark Strategy
#
# for_monotonous_timestamps()
#
# Means:
# Events are arriving in order
# ---------------------------------------------------------

watermark_strategy = WatermarkStrategy \
    .for_monotonous_timestamps() \
    .with_timestamp_assigner(
        MyTimestampAssigner()
    )


# ---------------------------------------------------------
# Step 6: Assign Timestamps and Watermarks
# ---------------------------------------------------------

timed_stream = ds.assign_timestamps_and_watermarks(
    watermark_strategy
)


# ---------------------------------------------------------
# Step 7: Reduce Function
#
# Calculates total sales
# ---------------------------------------------------------

class SumSales(ReduceFunction):

    def reduce(self, value1, value2):

        # value format:
        # (timestamp, shop_name, sales)

        return (
            value2[0],          # latest timestamp
            value1[1],          # shop name
            value1[2] + value2[2]
        )


# ---------------------------------------------------------
# Step 8: Apply Sliding Event Time Window
#
# Window Size = 10 seconds
# Slide Size = 5 seconds
#
# Means:
# Every 5 seconds,
# calculate sales of last 10 seconds
# ---------------------------------------------------------

result = timed_stream \
    .key_by(lambda x: x[1]) \
    .window(
        SlidingEventTimeWindows.of(
            Time.seconds(10),   # window size
            Time.seconds(5)     # sliding interval
        )
    ) \
    .reduce(SumSales())


# ---------------------------------------------------------
# Step 9: Print Output
# ---------------------------------------------------------

result.print()


# ---------------------------------------------------------
# Step 10: Execute Program
# ---------------------------------------------------------

env.execute(
    "Sliding Event Time Window Example"
)

'''
Important Concepts
Concept                                 	Meaning
Event Time	                                Time inside the event data
Watermark	                                Tracks event progress
Timestamp Assigner	                        Extracts timestamp from records
Sliding Window	                            Window moves continuously
ReduceFunction	                            Aggregates data
key_by()	                                Groups records by key
'''


# Window Working
'''
Window Size = 10 sec
Slide = 5 sec

Windows become:

Window	Data Included
0–10 sec	5000, 7000
5–15 sec	5000, 7000, 12000
10–20 sec	12000, 15000
15–25 sec	15000, 22000
'''