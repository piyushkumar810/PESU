'''
Q3. Event Time Tumbling Window
Question

Write a PyFlink program to:

Create a DataStream
Extract Event Time
Assign Watermarks
Group by Customer ID
Apply 5-second Tumbling Event Time Window
Compute total amount per customer

Input:

(A,100,1000)
(A,50,2000)
(B,30,3000)
(A,70,7000)
Solution
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.watermark_strategy import WatermarkStrategy
from pyflink.common.time import Duration
from pyflink.common.typeinfo import Types
from pyflink.datastream.window import TumblingEventTimeWindows
from pyflink.datastream.window import Time

# Create Environment
env = StreamExecutionEnvironment.get_execution_environment()

# Create DataStream
ds = env.from_collection([
    ("A",100,1000),
    ("A",50,2000),
    ("B",30,3000),
    ("A",70,7000)
])

# Assign Event Time & Watermarks
watermarked = ds.assign_timestamps_and_watermarks(
    WatermarkStrategy
        .for_bounded_out_of_orderness(Duration.of_seconds(2))
        .with_timestamp_assigner(lambda event, ts: event[2])
)

# Group by Customer
result = (
    watermarked
    .key_by(lambda x: x[0], key_type=Types.STRING())
    .window(TumblingEventTimeWindows.of(Time.seconds(5)))
    .reduce(lambda a,b:(a[0],a[1]+b[1],b[2]))
)

# Print Output
result.print()

# Execute
env.execute("Event Time Tumbling Window")
Window Formation
Window 0–5 sec

(A,100)

(A,50)

(B,30)

↓

A =150

B =30

-----------------

Window 5–10 sec

(A,70)

↓

A =70
Q4. Event Time Sliding Window
Question

Write a PyFlink program using:

Event Time
Sliding Window
Size = 5 sec
Slide = 2 sec

Input

(A,10,1000)
(A,20,3000)
(A,30,6000)
(A,40,8000)
Solution
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.watermark_strategy import WatermarkStrategy
from pyflink.common.time import Duration
from pyflink.common.typeinfo import Types
from pyflink.datastream.window import SlidingEventTimeWindows
from pyflink.datastream.window import Time

env = StreamExecutionEnvironment.get_execution_environment()

ds = env.from_collection([
    ("A",10,1000),
    ("A",20,3000),
    ("A",30,6000),
    ("A",40,8000)
])

watermarked = ds.assign_timestamps_and_watermarks(
    WatermarkStrategy
        .for_bounded_out_of_orderness(Duration.of_seconds(2))
        .with_timestamp_assigner(lambda event, ts: event[2])
)

result = (
    watermarked
    .key_by(lambda x:x[0], key_type=Types.STRING())
    .window(
        SlidingEventTimeWindows.of(
            Time.seconds(5),
            Time.seconds(2)
        )
    )
    .reduce(lambda a,b:(a[0],a[1]+b[1],b[2]))
)

result.print()

env.execute("Sliding Window")
Window Formation
Window 0-5

10

20

↓

30

----------------

Window 2-7

20

30

↓

50

----------------

Window 4-9

30

40

↓

70

Output

30

50

70
Q5. Session Window
Question

Gap = 10 seconds

Input

(A,10,1000)
(A,20,3000)
(A,30,16000)
(A,40,18000)

Compute total amount using Session Window.

Solution
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.watermark_strategy import WatermarkStrategy
from pyflink.common.time import Duration
from pyflink.common.typeinfo import Types
from pyflink.datastream.window import EventTimeSessionWindows
from pyflink.datastream.window import Time

env = StreamExecutionEnvironment.get_execution_environment()

ds = env.from_collection([
    ("A",10,1000),
    ("A",20,3000),
    ("A",30,16000),
    ("A",40,18000)
])

watermarked = ds.assign_timestamps_and_watermarks(
    WatermarkStrategy
        .for_bounded_out_of_orderness(Duration.of_seconds(2))
        .with_timestamp_assigner(lambda event, ts: event[2])
)

result = (
    watermarked
    .key_by(lambda x:x[0], key_type=Types.STRING())
    .window(
        EventTimeSessionWindows.with_gap(
            Time.seconds(10)
        )
    )
    .reduce(lambda a,b:(a[0],a[1]+b[1],b[2]))
)

result.print()

env.execute("Session Window")
Session Formation
1000

↓

3000

Gap =2 sec

↓

Same Session

↓

10+20

↓

30

-------------------

16000

↓

Gap =13 sec

↓

New Session

↓

16000

18000

↓

30+40

↓

70

Output

Session 1

A=30

----------------

Session 2

A=70
⭐ Exam Memory Trick

Almost every Event Time Window program has the same structure:

Create Environment
        ↓
Create DataStream
        ↓
Assign Timestamp
        ↓
Assign Watermarks
        ↓
key_by()
        ↓
Choose Window
        ↓
reduce()
        ↓
print()
        ↓
env.execute()
'''