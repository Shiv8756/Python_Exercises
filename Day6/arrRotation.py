def arrayRotation(l1,k):
    rotated_arr=l1[k:]+l1[:k]
    return rotated_arr

print(arrayRotation([1,2,3,4,5],2))