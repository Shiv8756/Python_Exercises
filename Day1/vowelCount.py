def countVowel(s):
    count=0
    for ch in s:
        if ch.lower() in "aeiou":
            count+=1
    return count

sentence = "Learning Python is fun!"
print(countVowel(sentence))