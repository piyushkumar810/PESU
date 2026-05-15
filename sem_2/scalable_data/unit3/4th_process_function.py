# ---------------------------------------------------------
# IMPORT REQUIRED CLASSES
# ---------------------------------------------------------

# Used to create Flink execution environment
from pyflink.datastream import StreamExecutionEnvironment

# Used to create custom Process Function
from pyflink.datastream.functions import ProcessFunction


# ---------------------------------------------------------
# CREATE CUSTOM PROCESS FUNCTION
# ---------------------------------------------------------
# ProcessFunction allows us to process each
# incoming record manually.
#
# Here we check:
# If value > 50  → High Value
# Else           → Normal Value
# ---------------------------------------------------------
class MyProcess(ProcessFunction):

    # -----------------------------------------------------
    # process_element()
    # -----------------------------------------------------
    # This method runs for EVERY incoming element.
    #
    # PARAMETERS:
    # value -> current input value
    # ctx   -> context information
    # -----------------------------------------------------
    def process_element(self, value, ctx):

        # Check whether value is greater than 50
        if value > 50:

            # yield sends output to next stream
            yield f"High Value: {value}"

        else:

            # Output for normal values
            yield f"Normal Value: {value}"


# ---------------------------------------------------------
# CREATE EXECUTION ENVIRONMENT
# ---------------------------------------------------------
# Main environment where Flink job runs
# ---------------------------------------------------------
env = StreamExecutionEnvironment.get_execution_environment()


# ---------------------------------------------------------
# CREATE INPUT DATA STREAM
# ---------------------------------------------------------
# from_collection() creates stream from Python list
#
# INPUT VALUES:
# 10
# 40
# 60
# 80
# ---------------------------------------------------------
ds = env.from_collection([10, 40, 60, 80])


# ---------------------------------------------------------
# APPLY PROCESS FUNCTION
# ---------------------------------------------------------
# ds.process(MyProcess())
#
# Every element goes inside process_element()
# one by one.
# ---------------------------------------------------------
processed_ds = ds.process(MyProcess())


# ---------------------------------------------------------
# PRINT OUTPUT
# ---------------------------------------------------------
processed_ds.print()


# ---------------------------------------------------------
# EXECUTE FLINK PROGRAM
# ---------------------------------------------------------
# Starts the Flink streaming job
# ---------------------------------------------------------
env.execute("Process Function Example")