s1 = "Abc"
s2 = "Xyz"
s3=""
if len(s1)==len(s2):
    for i in range(len(s1)):
        s3+=s1[i]+s2[i]

print(s3)