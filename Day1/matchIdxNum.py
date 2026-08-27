def MatchingIdxNum(l1):
    if l1[0]==l1[-1]:
        return True
    else:
        return False

numbers_x = [10, 20, 30, 40, 10]
print(MatchingIdxNum(numbers_x))