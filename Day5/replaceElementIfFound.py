l1=[5, 10, 15, 20, 25]
target=20
if target in l1:
    idx=l1.index(target)
    l1[idx]=200

print(l1)