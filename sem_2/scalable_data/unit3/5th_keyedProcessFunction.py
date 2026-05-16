# ---------------------------------------------------------
# IMPORT REQUIRED CLASSES
# ---------------------------------------------------------

# StreamExecutionEnvironment is used
# to create the Flink execution environment
from pyflink.datastream import StreamExecutionEnvironment

# KeyedProcessFunction is used for
# processing grouped/keyed streams
from pyflink.datastream.functions import KeyedProcessFunction


# ---------------------------------------------------------
# CREATE CUSTOM KEYED PROCESS FUNCTION
# ---------------------------------------------------------
# KeyedProcessFunction works only on
# grouped streams created using key_by().
#
# It processes records separately
# for every key/group.
#
# Example Groups:
#
# Alice -> all Alice records
# Bob   -> all Bob records
# ---------------------------------------------------------
class CountProc(KeyedProcessFunction):


    # -----------------------------------------------------
    # process_element()
    # -----------------------------------------------------
    # This method runs for every incoming record
    # inside each group.
    #
    # PARAMETERS:
    #
    # self  -> current object reference
    #
    # value -> current input record
    #          Example:
    #          ("Alice", 90)
    #
    # ctx   -> context object
    #          Used for timers/state information
    # -----------------------------------------------------
    def process_element(self, value, ctx):


        # -------------------------------------------------
        # value[0]
        # -------------------------------------------------
        # First element of tuple
        # Student Name
        #
        # Example:
        # value[0] = "Alice"
        # -------------------------------------------------


        # -------------------------------------------------
        # value[1]
        # -------------------------------------------------
        # Second element of tuple
        # Student Marks
        #
        # Example:
        # value[1] = 90
        # -------------------------------------------------


        # -------------------------------------------------
        # yield
        # -------------------------------------------------
        # Used to send/output processed data
        # to the next stream.
        # -------------------------------------------------
        yield (value[0], value[1])



# ---------------------------------------------------------
# CREATE EXECUTION ENVIRONMENT
# ---------------------------------------------------------
# Main Flink environment where
# the streaming job executes.
# ---------------------------------------------------------
env = StreamExecutionEnvironment.get_execution_environment()



# ---------------------------------------------------------
# INPUT DATA
# ---------------------------------------------------------
# Each tuple contains:
#
# (Student Name, Marks)
#
# Example:
# ("Alice", 90)
#
# Means:
# Student Alice scored 90 marks
# ---------------------------------------------------------
data = [

    ("Alice", 90),
    ("Bob", 80),
    ("Alice", 95),
    ("BOB", 85)

]



# ---------------------------------------------------------
# CREATE DATA STREAM
# ---------------------------------------------------------
# from_collection()
#
# Converts Python list into
# Flink DataStream.
# ---------------------------------------------------------
ds = env.from_collection(data)



# ---------------------------------------------------------
# key_by()
# ---------------------------------------------------------
# key_by(lambda x: x[0])
#
# Used to group records.
#
# x[0] means:
# First element of tuple
# which is Student Name.
#
# GROUPS CREATED:
#
# Alice -> (90, 95)
#
# Bob -> (80)
#
# BOB -> (85)
#
# IMPORTANT:
# Bob and BOB are treated
# as different groups because
# Flink is case-sensitive.
# ---------------------------------------------------------



# ---------------------------------------------------------
# APPLY KEYED PROCESS FUNCTION
# ---------------------------------------------------------
# process(CountProc())
#
# Sends every grouped record
# into process_element().
# ---------------------------------------------------------
result = ds.key_by(

    lambda x: x[0]

).process(CountProc())



# ---------------------------------------------------------
# PRINT OUTPUT
# ---------------------------------------------------------
# Displays output on console.
# ---------------------------------------------------------
result.print()



# ---------------------------------------------------------
# EXECUTE FLINK PROGRAM
# ---------------------------------------------------------
# Starts execution of Flink job.
# ---------------------------------------------------------
env.execute("Keyed Process Function Example")