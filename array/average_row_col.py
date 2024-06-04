from typing import List

def averageColumnMinimum(matrix: List[List[int]]) -> float:
    n = len(matrix)
    m = len(matrix[0])
    if m == 0:
        return 0
    
    sum = 0
    
    for j in range(m):
        min_num = float('inf')
        for i in range(n):
            if matrix[i][j] < min_num:
                min_num = matrix[i][j]
        sum += min_num

    return sum // m



def averageRowMinimum(matrix: List[List[int]]) -> float:
    n = len(matrix)
    m = len(matrix[0])
    if n == 0 or m == 0:
        return 0
    
    sum = 0

    for i in range(n):
        min_num = float('inf')
        for j in range(m):
            min_num = min(min_num, matrix[i][j])
        sum += min_num

    return sum // n



matrix = [
  [32, 23, 3],
  [23,  7, 5]]
print(averageColumnMinimum(matrix) == 11) # average(23, 7, 3) = 11
print(averageRowMinimum(matrix) == 4) # average(5, 3) = 4

matrix = [[]]
print(averageColumnMinimum(matrix) == 0)
print(averageRowMinimum(matrix) == 0)

matrix = [[5]]
print(averageColumnMinimum(matrix) == 5)
print(averageRowMinimum(matrix) == 5)

matrix = [[1, 2, 3]]
print(averageColumnMinimum(matrix) == 2)
print(averageRowMinimum(matrix) == 1)

matrix = [
  [1],
  [4],
  [7]]
print(averageColumnMinimum(matrix) == 1)
print(averageRowMinimum(matrix) == 4)

matrix = [
  [5, 5, 5],
  [5, 5, 5]]
print(averageColumnMinimum(matrix) == 5)
print(averageRowMinimum(matrix) == 5)



matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]]
print(averageColumnMinimum(matrix) == 2)
print(averageRowMinimum(matrix) == 4)

matrix = [
  [ 1,  2,  3,  4,  5],
  [ 6,  7,  8,  9, 10],
  [11, 12, 13, 14, 15]]
print(averageColumnMinimum(matrix) == 3)
print(averageRowMinimum(matrix) == 6)