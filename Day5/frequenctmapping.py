l1=[1, 3, 3, 2, 1, 1, 4, 3, 3]
d1={}
for i in l1:
    d1[i]=d1.get(i,0)+1

#print(d1)
mode=max(d1.items(),key=lambda k:k[1])
print(mode[0])