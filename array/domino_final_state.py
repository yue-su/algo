'''
You're given an array containing either '.', 'L', or 'R' values. These values represent a starting state of a row of dominoes. L means the domino has been pushed to the left. R means the domino has been pushed to the right. All elements to the left  of an L get pushed to the left and all elements to the right of an R get pushed to the right. If a domino is pushed in both directions simultaneously, it stays up.

Given the starting state array, return the updated array representing the final state of the dominos. All dominos should be L, R or . if it stays standing upright.
 

EXAMPLE(S)
[., L, ., R, .] -> [L, L, ., R, R]
[., R, ., ., L, .] -> [., R, R, L, L, .]
[., R, ., ., ., L, .] -> [., R, R, .,  L, L, .]

[L, ., ., ., ., ., ., ., R]
 s. f
FUNCTION SIGNATURE
def finalDominosState(dominosRow: list[str]):
'''


def finalDominosState(dominosRow: list[str]):
    def process(left, right):
        if dominosRow[left] == 'R' and dominosRow[right] == 'L':
            while left < right:
                dominosRow[left] = 'R'
                dominosRow[right] = 'L'
                left += 1
                right -= 1
            if left == right:
                dominosRow[left] = '.'
        else:
            d = '.'
            if dominosRow[left] == 'R':
                d = 'R'
            if dominosRow[right] == 'L':
                d = 'L'
            for i in range(left + 1, right):
                dominosRow[i] = d

    print("initial state: ", dominosRow)
    dominosRow = ['.'] + dominosRow + ['.']
    slow, fast = 0, 1
    while fast < len(dominosRow) - 1:
        while fast < len(dominosRow) - 1 and dominosRow[fast] == '.':
            fast += 1
        process(slow, fast)
        slow = fast
        fast += 1
    print("final   state: ", dominosRow[1:-1])


finalDominosState(['.', 'R', '.', '.', '.', 'L'])
finalDominosState(['.', 'R', '.', '.', 'L', '.'])
finalDominosState(['.', 'R', '.', '.', '.', '.'])
finalDominosState(['.', '.', '.', 'L', '.', '.'])
finalDominosState(['.', 'L', '.', 'R', '.', '.'])
finalDominosState(['R', '.', '.', 'L', '.', '.', 'R', '.', ',', 'L'])
