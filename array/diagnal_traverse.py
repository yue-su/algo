def findDiagonalOrder(mat: list[list[int]]) -> list[int]:
    row = 0
    col = 0
    res = []
    m = len(mat)
    n = len(mat[0])

    while len(res) < m * n:
        res.append(mat[row][col])
        if (row + col) % 2 == 0:
            if col == n - 1:
                row += 1
            elif row == 0:
                col += 1
            else:
                row -= 1
                col += 1
        else:
            if row == m - 1:
                col += 1
            elif col == 0:
                row += 1
            else:
                row += 1
                col -= 1

    return res


print(findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
      1, 2, 4, 7, 5, 3, 6, 8, 9])
