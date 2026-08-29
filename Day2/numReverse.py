def numReverse(num):
    result=0
    while num>0:
        n=num%10
        result=(result*10)+n
        num=num//10
    return result

print(numReverse(2345))