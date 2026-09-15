l1=[['apple', 'banana'], ['cherry', 'date']]

# for i in range(len(l1)):
#     for j in range(len(l1[i])):
#         l1[i].append("elderberry")
#
# print(l1)

for x in l1:
    print(x)
    x.append("elderberry")

print(l1)
