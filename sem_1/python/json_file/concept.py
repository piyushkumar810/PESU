# -------------------------- some important concepts      

# 1 json.load() → FILE ➜ PYTHON OBJECT
'''
📌 Meaning:-
Reads JSON from a file and converts it into a Python dictionary or list

📁 Example JSON file (data.json)
{
  "name": "Alice",
  "age": 25,
  "skills": ["Python", "Java"]
}

🧪 Python Code
'''
import json

with open("C://Users//piyush kumar//OneDrive//Desktop//GitHub//PESU//sem_1//python//json_file//data.json", "r") as f:
    data = json.load(f)

print(data)
print(type(data))
'''
✅ Output
{'name': 'Alice', 'age': 25, 'skills': ['Python', 'Java']}
<class 'dict'>


✔ File → Python dict
✔ Used when JSON is stored in a file
'''


# 2️⃣ json.loads() → STRING ➜ PYTHON OBJECT
'''
📌 Meaning:-
Reads JSON from a string and converts it into a Python object

🧪 Python Code
'''
import json
json_string = '{"name": "Bob", "age": 30}'
data = json.loads(json_string)

print(data)
print(type(data))
'''
✅ Output
{'name': 'Bob', 'age': 30}
<class 'dict'>

✔ String → Python dict
✔ Used when JSON comes from API / variable / text
'''
# ----------------------------------- note--------------------------
# 🔴 COMMON MISTAKE (EXAM TRAP)
# json.loads({"name": "Bob"})   # ❌ WRONG

# ❌ Because loads() expects a string, not a dictionary.



# 3️⃣ json.dump() → PYTHON OBJECT ➜ FILE
'''
📌 Meaning:-
Converts a Python object into JSON and writes it to a file
🧪 Python Code
'''

import json

data={
    "name":"piyush",
    "course":"MCA",
    "age":22,
    "college_allocated":"PESU"
}

with open("C://Users//piyush kumar//OneDrive//Desktop//GitHub//PESU//sem_1//python//json_file//data1.json","w") as file:
    json.dump(data,file)

'''
#📁 Output file (output.json)
#{"name": "Charlie", "age": 28, "married": false}

✔ Python dict → JSON file
✔ Used to store data permanently

🔴 COMMON MISTAKE (EXAM TRAP)
json.dump(data, "output.json")   # ❌ WRONG

❌ dump() needs a file object, not filename.
'''



# 4️⃣ json.dumps() → PYTHON OBJECT ➜ STRING
'''
📌 Meaning:-
Converts a Python object into a JSON string

🧪 Python Code
'''

import json

data = {
    "name": "Daisy",
    "age": 22,
    "children": None
}

json_string = json.dumps(data)

print(json_string)
print(type(json_string))
'''
✅ Output
{"name": "Daisy", "age": 22, "children": null}
<class 'str'>


✔ Python dict → JSON string
✔ Used for APIs, printing, sending data
'''

# 🔥 Pretty Printing (Very Common in Exams)
json.dumps(data, indent=4, sort_keys=True)
'''
Output
{
    "age": 22,
    "children": null,
    "name": "Daisy"
}
'''


# 🧠 FINAL ONE-LOOK SUMMARY (EXAM READY ⭐)
'''
Function	         Input	              Output	               Used When
-------------------------------------------------------------------------------------
json.load()	          File	           dict / list	             Read JSON file
json.loads()	     String	           dict / list	             Read JSON string
json.dump()	      dict / list	           File               	 Write JSON to file
json.dumps()	  dict / list	          String                 Convert to JSON text
'''