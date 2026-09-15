d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 20, "c": 30, "d": 40}
l1=[]
for i,j in d1.items():
    if i in d2:
        l1.append(i)

print(l1)

