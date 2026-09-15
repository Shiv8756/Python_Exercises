l1=[45, 12, 89, 2, 67]
largest=float('-inf')
smallest=float('inf')

for i in l1:
    if i>largest:
        largest=i
    if i<smallest:
        smallest=i

print(largest)
print(smallest)