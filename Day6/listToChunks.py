l1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n=3
l2=[]

for i in range(0,len(l1),n):
    l2.append(l1[i:i+n])
    #n=n+n

print(l2)

l3=[l1[i:i+n] for i in range(0,len(l1),n)]
print(l3)