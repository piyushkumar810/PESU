from pyflink.datastream import StreamExecutionEnvironment

# =====================================================
# Create Environment
# =====================================================
env = StreamExecutionEnvironment.get_execution_environment()

# =====================================================
# Case 1: Static List and Print
# =====================================================
print("\n===== CASE 1 =====")

ds1 = env.from_collection([10, 20, 30, 40, 50])
ds1.print()

# =====================================================
# Case 2: map() Multiply by 10
# =====================================================
print("\n===== CASE 2 =====")

ds2 = env.from_collection([1, 2, 3, 4, 5])

result2 = ds2.map(lambda x: x * 10)
result2.print()

# =====================================================
# Case 3: filter() Values > 50
# =====================================================
print("\n===== CASE 3 =====")

ds3 = env.from_collection([10, 25, 60, 75, 40, 90])

result3 = ds3.filter(lambda x: x > 50)
result3.print()

# =====================================================
# Case 4: flat_map() Split Sentences
# =====================================================
print("\n===== CASE 4 =====")

sentences = [
    "hello world",
    "welcome to pyflink",
    "data stream processing"
]

ds4 = env.from_collection(sentences)

result4 = ds4.flat_map(lambda line: line.split())
result4.print()

# =====================================================
# Case 5: key_by() Customer
# =====================================================
print("\n===== CASE 5 =====")

data5 = [
    ("Alice", 100),
    ("Bob", 200),
    ("Alice", 300),
    ("Bob", 150)
]

ds5 = env.from_collection(data5)

result5 = ds5.key_by(lambda x: x[0])
result5.print()

# =====================================================
# Case 6: reduce() Running Total
# =====================================================
print("\n===== CASE 6 =====")

data6 = [
    ("Alice", 100),
    ("Bob", 200),
    ("Alice", 300),
    ("Bob", 150),
    ("Alice", 50)
]

ds6 = env.from_collection(data6)

result6 = (
    ds6.key_by(lambda x: x[0])
       .reduce(lambda a, b: (a[0], a[1] + b[1]))
)

result6.print()

# =====================================================
# Execute
# =====================================================
env.execute("All PyFlink Cases")