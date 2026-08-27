def minMax(l1):
    smallest=999
    largest=0
    for i in l1:
        if i > largest:
            largest=i
        if i < smallest:
            smallest=i
            
    return largest,smallest
nums = [45, 2, 89, 12, 7]
val=minMax(nums)
print("min ",val[1], "max ",val[0])