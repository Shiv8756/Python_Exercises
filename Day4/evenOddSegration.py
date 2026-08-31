l1=[1, 2, 3, 4, 5, 6]
l2=[x for x in l1 if x%2==0]
l3=[x for x in l1 if x%2!=0]
l2.extend(l3)
print(l2)

