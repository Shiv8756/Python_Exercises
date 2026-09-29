import json
person = {"name": "Alice", "age": 30, "address": {"city": "Mumbai", "pin": "400001"}}
d=json.dumps(person)
print(d)