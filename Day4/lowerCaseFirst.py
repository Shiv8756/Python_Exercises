str1="PyNaTive"
s1=""
s2=""
for i in str1:
    if i.islower():
        s1+=i
    else:
        s2+=i
        
print(s1+s2)