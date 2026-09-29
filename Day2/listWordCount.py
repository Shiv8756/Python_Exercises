words = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

for i in words:
    print(i,len(i), end=" ")

count={words[i]:len(words[i]) for i in range(len(words))}

print(count)