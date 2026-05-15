from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.typeinfo import Types


# ---------------------------------------------------------
# FUNCTION: max_transaction()
# ---------------------------------------------------------
# This function is used inside reduce().
#
# PURPOSE:
# Compare two transactions of the same account
# and return the transaction having the
# maximum amount.
#
# Example:
# t1 = ("ACC101", 5000)
# t2 = ("ACC101", 8500)
#
# Since 8500 > 5000
# return ("ACC101", 8500)
# ---------------------------------------------------------
def max_transaction(t1, t2):

    # Compare transaction amounts
    if t1[1] >= t2[1]:

        # Return first transaction if amount is greater
        return t1

    # Otherwise return second transaction
    return t2


# ---------------------------------------------------------
# STEP 1: CREATE FLINK EXECUTION ENVIRONMENT
# ---------------------------------------------------------
# This is the main environment where
# the streaming job will run.
# ---------------------------------------------------------
env = StreamExecutionEnvironment.get_execution_environment()


# ---------------------------------------------------------
# STEP 2: CREATE INPUT STREAM
# ---------------------------------------------------------
# from_collection() creates a data stream
# from the given Python list.
#
# Each tuple contains:
# (Account Number, Transaction Amount)
#
# Example:
# ("ACC101", 5000)
#
# Means:
# Account ACC101 made transaction of 5000
# ---------------------------------------------------------
transactions = env.from_collection(

    [
        ("ACC101", 5000),
        ("ACC102", 7000),
        ("ACC101", 8500),
        ("ACC103", 3000),
        ("ACC102", 6500),
        ("ACC101", 4000)
    ],

    # -----------------------------------------------------
    # DEFINE DATA TYPES
    # -----------------------------------------------------
    # Tuple contains:
    # 1st value -> STRING
    # 2nd value -> INTEGER
    # -----------------------------------------------------
    type_info=Types.TUPLE([
        Types.STRING(),
        Types.INT()
    ])
)


# ---------------------------------------------------------
# STEP 3: GROUP DATA USING key_by()
# ---------------------------------------------------------
# key_by(lambda x: x[0])
#
# x[0] means Account Number
#
# All records having same account number
# are grouped together.
#
# GROUPS CREATED:
#
# ACC101 -> (5000, 8500, 4000)
# ACC102 -> (7000, 6500)
# ACC103 -> (3000)
# ---------------------------------------------------------


# ---------------------------------------------------------
# STEP 4: APPLY reduce()
# ---------------------------------------------------------
# reduce(max_transaction)
#
# reduce() continuously compares records
# inside each group.
#
# It keeps only the maximum transaction.
#
# FLOW:
#
# ACC101:
# Compare 5000 and 8500 -> keep 8500
# Compare 8500 and 4000 -> keep 8500
#
# Final:
# ("ACC101", 8500)
#
#
# ACC102:
# Compare 7000 and 6500 -> keep 7000
#
# Final:
# ("ACC102", 7000)
#
#
# ACC103:
# Only one value -> 3000
#
# Final:
# ("ACC103", 3000)
# ---------------------------------------------------------
max_per_account = transactions.key_by(

    # Group using account number
    lambda x: x[0],

    # Key data type
    key_type=Types.STRING()

).reduce(max_transaction)


# ---------------------------------------------------------
# STEP 5: PRINT OUTPUT
# ---------------------------------------------------------
# Output stream will display:
#
# (ACC101, 8500)
# (ACC102, 7000)
# (ACC103, 3000)
# ---------------------------------------------------------
max_per_account.print()


# ---------------------------------------------------------
# STEP 6: EXECUTE FLINK JOB
# ---------------------------------------------------------
# Starts execution of the streaming program.
# ---------------------------------------------------------
env.execute("reduce-maximum-transaction-per-account")