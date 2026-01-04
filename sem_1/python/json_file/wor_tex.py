import json

# Python dictionary
name_dict = {
    "name": "Andromeda",
    "languages": ["English", "French"],
    "married": True,
    "age": 32
}

# Write dictionary as JSON to file
with open("C:\\Users\\piyush kumar\\OneDrive\\Desktop\\GitHub\\PESU\\sem_1\\python\\json_file\\name.txt", "w", encoding="utf-8") as json_file:
    json.dump(name_dict, json_file, indent=4)

print("JSON data written to name.txt successfully")
