def divisibleBy5(l1):
    num=[x for x in l1 if x%5==0]
    return num
num_list = [10, 20, 33, 46, 55]
print(divisibleBy5(num_list))