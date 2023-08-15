import json

data = {"name" : 'John',
        "Age" : 30}
json_string = json.dumps(data)

print(data)
print(json_string)