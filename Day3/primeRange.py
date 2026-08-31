for i in range(3,20):
    for j in range(3,i):
        if i%j==0:
            #print(i,end=" ")
            break
    else:
        print(i)