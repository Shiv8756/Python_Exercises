l1=[1, 2, 3]
l2=[[]]
for i in range(0,len(l1)+1):
    for j in range(i+1,len(l1)+1):
        l2.append(l1[i:j])
print(l2)