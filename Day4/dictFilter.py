scores = {"Alice": 85, "Bob": 70, "Charlie": 95, "David": 60}
threshold = 75
d1={}
for key,value in scores.items():
    if value>threshold:
        d1[key]=value

print(d1)
