import json

# Open the JSON file in read mode
with open("C:\\Users\\piyush kumar\\OneDrive\\Desktop\\GitHub\\PESU\\sem_1\\python\\json_file\\emp.json", "r", encoding="utf-8") as file:
    jsonData = json.load(file)

# Print type of JSON object
print("Type of JSON object:", type(jsonData))
print()

# Traversing the JSON data
for name in jsonData:
    print("Name:", name)
    print("Phone Number:", jsonData[name]["number"])
    print("Age:", jsonData[name]["age"])

    print("Address:")
    for line in jsonData[name]["address"]:
        print("-", line)

    print("-" * 30)
