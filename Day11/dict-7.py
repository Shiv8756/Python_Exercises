original = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}
d= {}
for x,y in original.items():
    d.setdefault(y,[]).append(x)
print(d)