# Q1) Sensor gives negative temperature values sometimes.
#      How do you filter invalid readings?

# ✅ Solution:
'''
df[df["Temperature"] >= 0]

🧠 Explanation:
Filtering removes noisy sensor data.
'''

# Q2) Find average sensor reading per sensor.
'''
✅ Solution:
df.groupby("SensorID")["Value"].mean()

🧠 Explanation:
Grouping aggregates continuous data.
'''

# Q3) Why is sensor data considered stream data and not static data?
'''
✅ Solution:
Generated continuously
Time-dependent
Often large volume

🧠 Explanation:
Sensor data arrives in real-time, not all at once.
'''