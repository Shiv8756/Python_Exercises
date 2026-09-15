data = {"banana": 3, "apple": 5, "cherry": 1, "date": 4}

d=dict(sorted(data.items(),key=lambda x:x[0]))
print(d)