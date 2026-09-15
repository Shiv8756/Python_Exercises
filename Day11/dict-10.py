n=9
flag=False
for i in range(3,n//2):
    if n%i==0:
        print("Not Prime")
        break
else:
    print("Prime")
