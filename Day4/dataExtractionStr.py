str1 = "PYnative29@#8496"
sum=0
count=0
for i in str1:
    if i.isdigit():
        count+=1
        sum+=int(i)

print(sum)
print(sum/count)
