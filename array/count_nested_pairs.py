
'''
Count Nested Arrays

Given a nested array where each element may be 1) an integer or 2) an array, whose elements themselves may be integers or further arrays, count the total number of arrays.

What is the shape or pattern of this nested array structure? There can be empty lists but never None/null.
 

EXAMPLE(S)
countArrays([1, 2, 3]) == 1
countArrays([1, [1, 2, 3], 3]) == 2
countArrays([1, [1, [1, [1, [1]]]]]) == 5
countArrays([]) == 1
 

FUNCTION SIGNATURE
function countArrays(array) {
def countArrays(nestedList: list) -> int:
'''


def countArrays(nestedList: list) -> int:
    if not nestedList:
        return 1

    res = 1
    p = 0
    while p < len(nestedList):
        if isinstance(nestedList[p], int):
            p += 1
        else:
            res += 1
            temp = nestedList[p]
            nestedList = temp
            p = 0

    return res


print(countArrays([1, 2, 3]))
print(countArrays([1, [1, 2, 3], 3]))
print(countArrays([1, [1, [1, [1, [1]]]]]))
print(countArrays([]))
