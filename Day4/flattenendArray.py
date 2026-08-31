nested_list = [[10, 20], [30, 40], [50, 60]]
new_list=[]
for i in nested_list:
    for j in i:
        new_list.append(j)

print(new_list)