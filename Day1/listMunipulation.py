def listMunipulation(l1,idx,newFruit):
    l1[idx]=newFruit
    return l1


fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(listMunipulation(fruits,1,"mango"))