# 🔷 4️⃣ PICKLE — PYTHON OBJECT STORAGE
# Q1 What is serialization?
'''
✅ Solution:
Converting Python object into byte stream for storage.
'''

# Q2) Write code to store and retrieve a dictionary using pickle.
# ✅ Solution:

import pickle

data = {"name": "Alice", "marks": [90, 85]}

with open("data.pkl", "wb") as f:
    pickle.dump(data, f)

with open("data.pkl", "rb") as f:
    new_data = pickle.load(f)

print(new_data)

'''
🧠 Explanation:

dump() → save
load() → retrieve
'''


# Q3) Why is Pickle considered unsafe?
'''
✅ Solution:
Executes arbitrary code during unpickling
Can cause security issues

🧠 Explanation:
Never load pickle from unknown sources.
'''

# 🔥 COMPARISON QUESTIONS (VERY IMPORTANT)
# Compare :-JSON and Pickle.
# ✅ Solution:
'''
JSON	                              Pickle
-------------------------------------------------
Text format                     	Binary
Language independent	           Python only
Safer	                          Unsafe if untrusted
Slower	                             Faster
'''

# Q14) When to use XML instead of Pandas?
'''
✅ Solution:

XML → hierarchical, nested data
Pandas → flat tabular data
'''


# Q15 (Advanced – Concept Integration ⭐)
# Match the data type with the correct tool:
'''
Data Type	                               Tool
------------------------------------------------------
Nested configuration	                    XML
Student marks table	                      Pandas
Temperature readings	               Sensor + Pandas
Python object graph	                        Pickle
'''