import json

data = {
    "name": "Daisy",
    "age": 22,
    "children": None
}

json_string = json.dumps(data)

print(json_string)
print(type(json_string))