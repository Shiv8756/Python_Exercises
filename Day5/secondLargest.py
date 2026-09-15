l1=[12, 35, 1, 10, 34, 1, 35]
largest=-999
second_largest=-999
l1=list(set(l1))
for i in l1:
    if i>largest:
        second_largest=largest
        largest = i
    elif i>second_largest :
        second_largest=i
print(second_largest)