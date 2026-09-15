def cumlativeSum(l1):
    sum=0
    l2=[]
    for i in l1:
        sum+=i
        l2.append(sum)
    return l2

print(cumlativeSum([10,20,30,40]))