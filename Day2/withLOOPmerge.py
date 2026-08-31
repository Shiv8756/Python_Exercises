
dict1 = {"name": "Alice", "age": 25}
dict2 = {"city": "New York", "job": "Engineer"}

#print(dict1 | dict2)

#print(dict1.update(dict2))

for key, value in dict2.items():
    dict1[key] = value

print(dict1)