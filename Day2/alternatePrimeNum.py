def alternatePrime(n):
    l2=[]
    for i in range(2,n+1):
        prime_num=checkPrime(i)
        if prime_num==True:
            l2.append(i)
    return l2


def checkPrime(n):
    for i in range(2,n+1):
        if n%i==0:
            return False
        return True

l1=alternatePrime(20)
print(l1[::2])