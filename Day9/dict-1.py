d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 20, "c": 30, "d": 40}
d3={}
for i,j in d1.items():
    if i in d2:
        d3[i]=j

print(d3)

