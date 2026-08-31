n=75896
largest=0
smallest=9

while n>0:
    temp=n%10
    if temp>largest:
        largest=temp
    if temp<smallest:
        smallest=temp

    n=n//10

print(largest)
print(smallest)