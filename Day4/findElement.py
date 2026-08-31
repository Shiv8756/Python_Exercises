matrix = [[10, 20], [30, 40], [50, 60]]
target=30

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if target==matrix[i][j]:
            print("row ",i," ","column ",j)
            break