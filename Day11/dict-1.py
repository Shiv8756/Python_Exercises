data = {"fruits": ["apple", "banana", "cherry"], "vegs": ["carrot"], "grains": ["rice", "wheat"]}

print(max(data.items(),key=lambda k:len(k[1]))[0])


