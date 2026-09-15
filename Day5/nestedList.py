l1=[[1, 2], [3, 4, 5], [6, 7]]
target=7
for i in range(len(l1)):
    for j in range(len(l1[i])):
        if l1[i][j]==target:
            print("Element found in the list")
            break
    else:
        print("Not in the nested list")

    #print("Element not found")