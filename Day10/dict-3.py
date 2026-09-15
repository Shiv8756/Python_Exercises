scores = {"Alice": 88, "Bob": 72, "Charlie": 95, "Diana": 60}
d=dict(sorted(scores.items(),key=lambda k:k[1]))
print(d)