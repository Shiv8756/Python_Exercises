data = {"a": 1, "b": 2, "c": 3, "d": 4}
l1=list(data.values())
is_unique=len(l1)==len(set(l1))
print(is_unique)
