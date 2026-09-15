import json
person = {"name": "Alice", "age": 30, "address": {"city": "Mumbai", "pin": "400001"}}
d=json.dumps(person,indent=4)
print(d)