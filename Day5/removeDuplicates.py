l1=[10, 20, 10, 30, 40, 40, 20, 50]
d1={}

for i in l1:
    if i in d1:
        d1[i] +=1
    d1[i]=1

print(d1.items())