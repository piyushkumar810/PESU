# ---------------------------- unit 3
'''
q1) Given:- Input Stream

(A,1)
(A,2)
(A,3)
(A,4)
(A,5)

Window:
CountSlidingWindowAssigner.of(3,1)

Meaning:
Window Size = 3
Slide = 1
'''

# solution
'''
Input

1   2   3   4   5

Window 1
---------
[1 2 3]
 Sum = 6

      ↓ Slide by 1

Window 2
---------
  [2 3 4]
   Sum = 9

      ↓ Slide by 1

Window 3
---------
    [3 4 5]
     Sum = 12
'''




# q2
'''
data = [
("A",10),
("B",20),
("A",15),
("B",5),
("A",30)
]

result = ds.key_by(lambda x:x[0]) \
           .reduce(lambda a,b:(a[0],a[1]+b[1]))

write thee output for each key
'''

# solution
'''
Incoming Stream

(A,10)
(B,20)
(A,15)
(B,5)
(A,30)

↓

key_by()

A → (10) (15) (30)

B → (20) (5)

↓

reduce()

A

10
↓

10+15 =25
↓

25+30 =55

Final A =55


B

20
↓

20+5 =25

Final B =25
'''


# q3
'''
Question

Write a complete PyFlink program to:

Create a stream from [5,10,15,20,25]
Filter values greater than 10
Multiply remaining values by 2
Print the output
'''
# solution
'''
from pyflink.datastream import StreamExecutionEnvironment
env=StreamExecutionEnvironment.get_execution_environment()

ds=env.from_collection([5,10,15,20,25])

filtered_ds=ds.filter(lambda x: x>10)

mapped_ds=filtered_ds.map(lambda x:x*2)

mapped_ds.print()

env.execute("basic transformation pipeline")
'''



# q4
'''
First Understand flat_map()

Input:
"flink stream processing"

If we use:
.split()

It becomes:
["flink", "stream", "processing"]

flat_map() outputs each word separately.
One input sentence → Multiple output records.
'''
# solution
'''
from pyflink.datastrem import StreamExecutionEnvironment
env=StreamExecutionEnvironment.get_execution_environment()

ds=env.from_collection([
"flink stream processing",
    "pyflink data stream"
])

resultant_ds=ds.flat_map(lambda x: x.split())

resultant_ds.print()

env.execute("word seprated")
'''


# q5
'''
Question

Write a complete PyFlink program for:

(A,100)
(B,200)
(A,50)
(B,75)
(A,25)

Group by customer ID and compute the running total spend.
'''
# solution
'''
from pyflink.datastrem import StreamExecutionEnvironment
from pyflink.common.typeinfo import Types

ds=env.form_collection([
("A",100),
("B",200),
("A",50),
("B",75),
("A",25)
])

grouped_ds=ds.key_by(lambda x:x[0] key_type=Types.STRING())

result=grouped_ds.reduce(lambda a,b: (a[0], a[1]+b[1]))

result.print()

env.execute("total spend by one id")
'''


# q6
'''
Question

Write a complete PyFlink program to:

Extract event time from index 2
Assign watermarks
Group by customer
Apply 5-second tumbling event-time window
Compute total amount per customer per window

Input:

(A,100,1000)
(A,50,2000)
(B,30,3000)
(A,70,7000)
'''
# understanding
'''
Step 1 : Understand the Data

Each record has 3 values.
(Customer, Amount, Timestamp)

Example:
(A,100,1000)

A      → Customer ID
100    → Amount
1000   → Event Time

Here,
x[0] → Customer
x[1] → Amount
x[2] → Timestamp
'''
# solution
'''# ------------------------------------
# Import
# ------------------------------------
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.typeinfo import Types

# ------------------------------------
# Create Environment
# ------------------------------------
env = StreamExecutionEnvironment.get_execution_environment()

# ------------------------------------
# Create DataStream
# ------------------------------------
ds = env.from_collection([
    ("A",100,1000),
    ("A",50,2000),
    ("B",30,3000),
    ("A",70,7000)
])

# ------------------------------------
# Assign Event Time
# (Timestamp at index 2)
# ------------------------------------
# Watermarks assigned here

# ------------------------------------
# Group by Customer
# ------------------------------------
keyed = ds.key_by(
    lambda x:x[0],
    key_type=Types.STRING()
)

# ------------------------------------
# Apply 5-second Tumbling Window
# ------------------------------------
# window(TumblingEventTimeWindows.of(Time.seconds(5)))

# ------------------------------------
# Sum Amount
# ------------------------------------
# reduce(lambda a,b:(a[0],a[1]+b[1],b[2]))

# ------------------------------------
# Print
# ------------------------------------
# result.print()

env.execute("Event Time Tumbling Window")
'''



# q7 Complete the missing code
'''
class RunningSpend(KeyedProcessFunction):

    def open(self, runtime_context):

        des = _______________________

        self.total_state = ______________________

    def process_element(self, value, ctx):

        current = ______________________

        if current is None:
            current = 0

        current = current + value[1]

        _______________________

        return [(value[0], current)]
'''
# solution
'''
from pyflink.datastream.state import ValueStateDescriptor
from pyflink.common.typeinfo import Types

class RunningSpend(KeyedProcessFunction):

    def open(self, runtime_context):

        des = ValueStateDescriptor(
            "total",
            Types.INT()
        )

        self.total_state = runtime_context.get_state(des)

    def process_element(self, value, ctx):

        current = self.total_state.value()

        if current is None:
            current = 0

        current = current + value[1]

        self.total_state.update(current)

        return [(value[0], current)]
'''
# flow
'''
New Record

(A,50)
        │
        ▼
Read State

100
        │
        ▼
Add

100+50
        │
        ▼
150
        │
        ▼
Update State

150
        │
        ▼
Return

(A,150)
'''



# q8  Code Snippet 2 – WindowFunction
# Question:
# Complete the following WindowFunction so that it returns:
'''
from pyflink.datastream.functions import WindowFunction

class SummaryWindow(WindowFunction):

    def apply(self,
              key,
              window,
              inputs):

        items = ______________________

        count = ______________________

        total = ______________________

        return [(
            ______________________,
            ______________________,
            ______________________
        )]
'''
# solution
'''
from pyflink.datastream.functions import WindowFunction

class SummaryWindow(WindowFunction):

    def apply(self,
              key,
              window,
              inputs):

        items = list(inputs)

        count = len(items)

        total = sum(x[1] for x in items)

        return [(
            key,
            count,
            total
        )]
'''

# flow
'''
items = list(inputs)
          ↓
Convert window data into a list

count = len(items)
          ↓
Count records

total = sum(x[1] for x in items)
          ↓
Add all values

return (key,count,total)
'''