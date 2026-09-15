data = {"name": "Alice", "age": None, "city": "Paris", "score": None}

d={x:y for x,y in data.items() if y!=None}
print(d)