product = {"id": 101, "name": "Laptop", "price": 999, "stock": 50, "warehouse": "A3"}
l1=["stock", "warehouse"]
# product.pop(*l1)
# print(product)

for i in l1:
    product.pop(i)

print(product)