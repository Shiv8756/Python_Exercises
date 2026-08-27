def removedup(l1):
    previous_num=0
    l2=[]
    for i in l1:
        if i in l2:
            continue
        else:
            l2.append(i)
    return l2
data = [1, 2, 2, 3, 4, 4, 4, 5]
print(removedup(data))