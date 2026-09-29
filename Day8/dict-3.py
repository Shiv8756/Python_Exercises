text = "hello world"
d={}
for i in text:
    if i not in  d:
        d[i]=0

    d[i]+=1


print(d)
