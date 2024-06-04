def diagonalSum(matrix):
    sum = 0
    if len(matrix) == 0:
        return sum

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == j:
                sum += matrix[i][j]
            
            if i + j == len(matrix) - 1 and i != j:
                sum += matrix[i][j]
    
    return sum



mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]
print(diagonalSum(mat) == 25)

mat = [[1,1,1,1],
       [1,1,1,1],
       [1,1,1,1],
       [1,1,1,1]]
print(diagonalSum(mat) == 8)

mat = [[5]]
print(diagonalSum(mat) == 5)

mat = []
print(diagonalSum(mat) == 0)