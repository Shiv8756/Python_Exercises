l1=[0, 1, 0, 3, 12]
l2=[]
for i in l1:
    if i==0:
        l1.remove(0)
        l1.append(0)

print(l1)