stock = {"apples": 34, "bananas": 12, "oranges": 57, "grapes": 8, "mangoes": 23}
smallest=999
smallest_key=""
for i,j in stock.items():
    if j<smallest:
        smallest=j
        smallest_key=i

print(smallest_key)