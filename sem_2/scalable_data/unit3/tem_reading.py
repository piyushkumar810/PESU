# PROGRAM 1 : PROCESSFUNCTION – FLAG HIGH TEMPERATURE READINGS
# Problem Statement
# 
# A city monitoring system receives temperature readings from different locations.
# 
# Write a PyFlink DataStream program using ProcessFunction to check each reading.
# 
# If temperature is greater than or equal to 38°C → mark it as "HIGH"
# Otherwise → mark it as "NORMAL"


# ---------------------------------------------------------
# IMPORT REQUIRED CLASSES
# ---------------------------------------------------------

# StreamExecutionEnvironment:
# Used to create the Flink streaming environment.
from pyflink.datastream import StreamExecutionEnvironment


# ProcessFunction:
# Used to process each incoming record one-by-one.
from pyflink.datastream.functions import ProcessFunction


# Types:
# Used to define output data types clearly.
from pyflink.common.typeinfo import Types



# ---------------------------------------------------------
# CREATE CUSTOM PROCESS FUNCTION
# ---------------------------------------------------------

# We create our own class.
# This class inherits ProcessFunction.

class TemperatureChecker(ProcessFunction):

    # process_element() runs for EVERY incoming record.
    #
    # Parameters:
    # value     -> current incoming data
    # ctx       -> context object (not used here)
    # collector -> used to send output

    def process_element(self, value, ctx):

        # value contains:
        # ('CityName', temperature)

        city = value[0]
        temp = value[1]



        # -------------------------------------------------
        # CHECK TEMPERATURE CONDITION
        # -------------------------------------------------

        # If temperature >= 38
        # mark as HIGH

        if temp >= 38:
            status = "HIGH"

        # Otherwise NORMAL

        else:
            status = "NORMAL"



        # -------------------------------------------------
        # SEND OUTPUT
        # -------------------------------------------------

        # collector.collect() emits/output the result

        collector.collect((city, temp, status))



# ---------------------------------------------------------
# CREATE EXECUTION ENVIRONMENT
# ---------------------------------------------------------

# This creates the main Flink environment.

env = StreamExecutionEnvironment.get_execution_environment()



# ---------------------------------------------------------
# CREATE INPUT STREAM
# ---------------------------------------------------------

# from_collection() creates stream from normal Python data.

data_stream = env.from_collection(

    [
        ("Delhi", 40),
        ("Mumbai", 35),
        ("Chennai", 39),
        ("Bangalore", 32),
        ("Hyderabad", 38)
    ],

    # Define input data type
    type_info=Types.TUPLE([Types.STRING(), Types.INT()])
)



# ---------------------------------------------------------
# APPLY PROCESS FUNCTION
# ---------------------------------------------------------

# process() applies custom ProcessFunction.

result_stream = data_stream.process(

    TemperatureChecker(),

    # Define output type
    output_type=Types.TUPLE([
        Types.STRING(),
        Types.INT(),
        Types.STRING()
    ])
)



# ---------------------------------------------------------
# PRINT OUTPUT
# ---------------------------------------------------------

# print() displays output in terminal.

result_stream.print()



# ---------------------------------------------------------
# START FLINK PROGRAM
# ---------------------------------------------------------

# execute() starts the streaming job.

env.execute("Temperature Monitoring System")



# ----------------------------------------- or

from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.functions import ProcessFunction
from pyflink.datastream.output_tag import OutputTag


# Create Process Function
class TemperatureProcess(ProcessFunction):

    def process_element(self, value, ctx):

        city = value[0]
        temp = value[1]

        if temp >= 38:
            status = "HIGH"
        else:
            status = "NORMAL"

        yield (city, temp, status)


# Create execution environment
env = StreamExecutionEnvironment.get_execution_environment()

# Sample temperature data
data = [
    ("Delhi", 40),
    ("Mumbai", 34),
    ("Chennai", 38),
    ("Bangalore", 29),
    ("Hyderabad", 41)
]

# Create DataStream
ds = env.from_collection(data)

# Apply Process Function
result = ds.process(TemperatureProcess())

# Print result
result.print()

# Execute program
env.execute("Temperature Monitoring System")