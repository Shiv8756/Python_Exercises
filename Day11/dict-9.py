words = ["apple", "avocado", "banana", "blueberry", "cherry", "apricot"]
d={}
for x in words:
    if x[0] not in d:
        d[x[0]]=[]
    d[x[0]].append(x)

print(d)