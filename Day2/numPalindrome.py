def palindromeCheck(num):
    result=0
    while num>0:
        n=num%10
        result=(result*10)+n
        num=num//10
    return result

num=121
result=palindromeCheck(num)

print(num==result)