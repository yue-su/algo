from test_case import Test, List


def sm(matrix: List[List[int]]) -> List[int]:
    if not matrix:
        return []
    # Write your code here.
    top = 0
    left = 0
    right = len(matrix[0]) - 1
    bottom = len(matrix) - 1

    res = []

    while left <= right and top <= bottom:
        if left <= right:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
        if top <= bottom:
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
        if top <= bottom:
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

    print(res)
    return res


test = Test("")
# Test Cases
test.startProblem("Spiral Matrix")
test.test([1, 2, 3, 6, 9, 8, 7, 4, 5], sm(
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 1)
test.test([1, 2, 3, 3, 3, 2, 1, 1, 2], sm(
    [[1, 2, 3], [1, 2, 3], [1, 2, 3]]), 2)
test.test([1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7], sm(
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]), 3)
test.test([], sm([]), 4)
test.test([1], sm([[1]]), 5)
test.endProblem()
