data = {"a": 1, "b": 2, "c": 3, "d": 2}
print(len(data.values())==len(list(set(data.values()))))