def strWordCount(st1,word):
    l=st1.split(" ")
    count=0
    for i in l:
        if i==word:
            count+=1
    return count
str= "Emma is good developer. Emma is a writer"
print(strWordCount(str,"Emma"))