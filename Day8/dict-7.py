scores = {"Alice": 88, "Bob": 95, "Carol": 72, "Dave": 95, "Eve": 84}
largest=0
largestName=""
for i,j in scores.items():
    if j>largest:
        largest=j
        largestName=i

print(largestName)