
'''
Reversi (https://en.wikipedia.org/wiki/Reversi), also called Othello, is a game where each piece has two sides, black and white, and after being placed, further moves cause other pieces to flip tiles. Specifically, a line of pieces of one color gets flipped when they become surrounded by pieces of the opposite color on both ends.

In this problem, we will be given a 2-dimensional array representing the board. Each position will contain a value of “B”, “W”, or “*” representing empty. Additionally, we get a position that is currently empty. Update the board to the new state after that play, including any flips if it is black’s turn to play. You can modify the existing array, but either way, return the board (2d array) with the new state.

EXAMPLE(S)
For example, consider the row:

1 2 3 4 5 6 7 8
* B W W W W * *

If black places a piece at position 7, the white pieces in between get flipped, so the result is:

1 2 3 4 5 6 7 8
* B B B B B B *

This can happen on a row, column, or diagonal and even at the same time. In the following example, if white place on position (5, 5), then all of the black pieces flip to white!

  1 2 3 4 5 6 7 8
1 * * * * * * * *
2 * * * W * * * *
3 * * W B * * * *
4 * * * W * * * *
5 W B B B ! * * *
6 * * * * B * * *
7 * * * * B * * *
8 * * * * W * * *
 

FUNCTION SIGNATURE
function reversi(board, x, y, c)
def reversi(board, x, y, c):

The follow up adds another parameter, c.

planning:

reversi(board, x, y, c):
  
  // [1, 0] -> right
  // [0, -1] -> down
  // [0, 1] => up
  // [-1, 0] -> left
  // []

  helper(a, b, dirs) {
    new postion a =  a + dirs[0], b = b + dirs[1]

    if new postion is * or out of boundary
      return false

    if new position is c:
      return true
    
    if (helper(new a and b) === true)
    mark is as c
    return true
    
    return false;

  }

  from the x, y position, 
  check in 8 directions
  for any of the direction,
    if curr pos is out of bound, 
      return false
    keep checking for the c color
    if at any point, * is found
      return false

    if c is found,
      return true
    mark is as c    
  return false

const directions = [
    [0, 1], // Up
    [1, 1], // Up and right
    [1, 0], // Right
    [1, -1], // Down and right
    [0, -1], // Down
    [-1, -1], // Down and left
    [-1, 0], // Left
    [-1, 1], // Up and left
  ];
  
'''
# */


def inbounds(grid, row, col):
  return row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0])


def reversi(board, x, y, c):

  directions = [(1, 0), (0, -1), (0, 1), (-1, 0),
                (-1, -1), (-1, 1), (1, -1), (1, 1)]

  def helper(a, b, dirs):
    if not inbounds(board, a, b):
      return False

    if board[a][b] == '*':
      return False

    if board[a][b] == c:
      return True

    if (helper(a + dirs[0], b + dirs[1], dirs) == True):
      board[a][b] = c
      return True

    return False

  for direction in directions:
    helper(x, y, direction)

  return board


def printBoard(board):
  for row in range(len(board)):
    print(" ".join(board[row]))

  # function printBoard(board) {
  # for (let i = 0; i < board.length; i++) {
  #   console.log(board[i].join(''));
  # }
  # console.log();
  # }


board = [
    ["B", "W", "*"],
    ["W", "W", "*"],
    ["*", "*", "*"],
]
reversi(board, 0, 2, "B")
printBoard(board)

print('***********************')

board = [
    ["B", "W", "*"],
    ["W", "W", "*"],
    ["*", "*", "*"],
]
reversi(board, 2, 0, "B")
printBoard(board)

print('***********************')

board = [
    ["B", "W", "*"],
    ["W", "W", "*"],
    ["*", "*", "*"],
]
reversi(board, 2, 2, "B")
printBoard(board)

print('***********************')

board = [
    ["*", "W", "B"],
    ["W", "W", "B"],
    ["B", "B", "B"],
]
reversi(board, 0, 0, "B")
printBoard(board)


'''
let board = [[null, null, "B", "W", "B", null]];
console.log(findAndFlipOneDirection(
   board, 0, 3, 0, 1, "B"
));
console.log(board);

board = [[null, null, "B", "W", "B", null]];
console.log(findAndFlipOneDirection(
   board, 0, 1, 0, -1, "B"
));
console.log(board);
'''
