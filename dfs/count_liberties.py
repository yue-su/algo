'''
Go is an ancient game played on a board of 19x19 grid of lines. Black and white stones are placed at the intersections of these lines. A group of stones of one color is considered a _connected_ if every stone in the group is reachable from every other, traveling horizontally or vertically. For example, the following shows a is a single connected white group because we can traverse through all stones without jumps or moving diagonally. 

  0 1 2 3 4 5
0 + + W + + +
1 + + W + + +
2 + + W W + +
3 + + + W W +
4 + + + + + +
5 + + + + + +

A connected group of stones is captured when *all* adjacent points to the group are occupied by stones of the opposite color. Unoccupied intersections adjacent to a group of stones are called _liberties_. While playing the game, players must keep track of their groups and their liberty counts to look for strong moves to play.

The previous example group of white stones has 10 liberties. If the stone at (2, 3) is removed, it would be broken into two groups. The vertical group of three has 7 liberties, and the horizontal group of two has 6:

  0 1 2 3 4 5
0 + + W + + +
1 + + W + + +
2 + + W + + +
3 + + + W W +
4 + + + + + +
5 + + + + + +

Given a 19x19 board and an occupied position on the board, count the liberties of that connected group. Assume that the board is square and, at most 19x19, the size of a real Go board.
 

EXAMPLE(S)
countLiberties(
  [
    ['+', '+', '+'],
    ['+', 'W', '+'],
    ['+', '+', '+'],
  ],
  1, 1) == 4

countLiberties(
  [
    ['+', '+', '+'],
    ['+', 'B', 'B'],
    ['+', '+', 'B'],
  ],
  1, 1) == 4

Similar to the last example, but the new stone isn't connected.
countLiberties(
  [
    ['B', '+', '+'],
    ['+', 'B', 'B'],
    ['+', '+', 'B'],
  ],
  1, 1) == 4

countLiberties(
  [
    ['W', '+', 'W'],
    ['W', 'B', 'B'],
    ['W', 'W', 'B'],
  ],
  1, 1) == 1
 

FUNCTION SIGNATURE
function countLiberties(board, x, y) {

'''


def countLiberties(board, x, y):
    deltas = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    color = board[x][y]
    visited = set()
    counter = 0

    def is_within_bounds(row, col):
        return 0 <= row < len(board) and 0 <= col < len(board[0])

    def helper(row, col):
        nonlocal counter
        # first check boundaries and if it is visited
        if not is_within_bounds(row, col) or (row, col) in visited:
            return
        # check if it's a '+'
        if board[row][col] == '+':
            counter += 1
            visited.add((row, col))
            return
        
        # only two posiblities left, either same color or oppsite
        if board[row][col] != color:
            return

        visited.add((row, col))

        for delta in deltas:
            new_row, new_col = row + delta[0], col + delta[1]
            helper(new_row, new_col)

    helper(x, y)

    return counter


print(countLiberties(
    [
      ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
      ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
        ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
        ['+', '+', 'B', 'B', 'B', 'B', 'B', '+', '+'],
        ['+', '+', 'B', '+', 'B', '+', 'B', '+', '+'],
        ['+', '+', 'B', 'B', 'B', 'B', 'B', '+', '+'],
        ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
        ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
        ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
      ],
    4, 4
), 18)

print(countLiberties(
    [
      ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
      ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
        ['+', 'W', 'W', 'W', 'W', 'W', 'W', 'W', '+'],
        ['+', 'W', 'B', 'B', 'B', 'B', 'B', 'W', '+'],
        ['+', 'W', 'B', '+', 'B', '+', 'B', 'W', '+'],
        ['+', 'W', 'B', 'B', 'B', 'B', 'B', 'W', '+'],
        ['+', 'W', 'W', 'W', 'W', 'W', 'W', 'W', '+'],
        ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
        ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
      ],
    4, 4
), 2)

print(countLiberties(
    [
      ['+', '+', '+', 'W', '+', '+', '+', '+', '+'],
      ['+', '+', '+', 'W', 'B', '+', '+', '+', '+'],
        ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
        ['W', 'W', 'W', '+', 'B', '+', '+', '+', '+'],
        ['B', 'B', '+', 'B', '+', '+', '+', '+', '+'],
        ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
        ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
        ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
        ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
      ],
    3, 2
), 5)

print(countLiberties(
    [
      ['+', '+', '+', 'W', '+', '+', '+', '+', '+'],
      ['+', '+', '+', 'W', 'B', '+', '+', '+', '+'],
        ['+', '+', '+', 'W', '+', '+', '+', '+', '+'],
        ['W', 'W', 'W', '+', 'B', '+', '+', '+', '+'],
        ['B', 'B', '+', 'B', '+', '+', '+', '+', '+'],
        ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
        ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
        ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
        ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
      ],
    3, 2
), 5)

print(countLiberties(
    [
      ['+', '+', '+', 'W', '+', '+', '+', '+', '+'],
      ['+', '+', '+', 'W', 'B', '+', '+', '+', '+'],
        ['+', '+', '+', 'W', '+', '+', '+', '+', '+'],
        ['W', 'W', 'W', 'W', 'B', '+', '+', '+', '+'],
        ['B', 'B', '+', 'B', '+', '+', '+', '+', '+'],
        ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
        ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
        ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
        ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
      ],
    3, 2
), 8)
