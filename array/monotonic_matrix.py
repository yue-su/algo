def search_matrix(matrix, target):
    i = 0
    j = len(matrix[0]) - 1

    while i < len(matrix) and j >= 0:
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] < target:
            i += 1
        else:
            j -= 1
    
    return False

# start from the top right corner

test1 = [
  [1,   5,   7,  10,  15],
  [3,   8,  10,  17,  20],
  [5,  11,  12,  18,  22],
  [9,  13,  19,  21,  25]
]

print(search_matrix(test1, 1), True)
print(search_matrix(test1, 25), True)
print(search_matrix(test1, 12), True)
print(search_matrix(test1, 10), True)
print(search_matrix(test1, 5), True)
print(search_matrix(test1, 21), True)

print(search_matrix(test1, 0), False)
print(search_matrix(test1, 27), False)
print(search_matrix(test1, 4), False)
print(search_matrix(test1, 24), False)
print(search_matrix(test1, 14), False)

test2 = [
  [1,   5,   7,  10],
  [3,   8,  10,  17],
  [5,  11,  12,  18],
  [9,  13,  19,  21]
]

print(search_matrix(test2, 1), True)
print(search_matrix(test2, 12), True)
print(search_matrix(test2, 10), True)
print(search_matrix(test2, 5), True)
print(search_matrix(test2, 21), True)

print(search_matrix(test2, 0), False)
print(search_matrix(test2, 27), False)
print(search_matrix(test2, 4), False)
print(search_matrix(test2, 24), False)
print(search_matrix(test2, 14), False)