l1=["PHP", "Exercises", "Backend", "Python"]
wordLen=0
word=""
for i in l1:
    if wordLen<len(i):
        word=i
        wordLen=len(i)

print(word)