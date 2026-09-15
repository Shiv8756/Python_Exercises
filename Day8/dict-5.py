scores = {"Alice": 82, "Bob": 45, "Carol": 91, "Dave": 58, "Eve": 73}

d={x:y for x,y in scores.items() if scores[x]>60}
print(d)