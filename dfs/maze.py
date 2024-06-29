"""

Given a description of a maze, find a path to successfully make it all the way through the maze.  The maze is represented by a 2D matrix where a " " character is a place where the player can move, and a "W" character represents a wall.  The character "S" indicates the start postiion, and "E" the end position.  Any number character "0" through "9" represents some amount of treasure at that location.  An "m" indicates a monster.  If you encounter a monster, it dies and the player is injured.  If you encounter a second monster, then the player dies.  You are permitted to retrace your steps.

Question 1: Find any path to escape the maze.
Question 2: Find the shortest path to escape the maze.
Question 3: Find a path where you don't get injured.
Question 4: Find a path where you collect the most treasure.

maze = [
  [ "W", "W", "S", "W", "W", "W", "W", "W" ],
  [ "W", " ", " ", "W", " ", " ", " ", "W" ],
  [ "W", " ", " ", " ", " ", "W", " ", "W" ],
  [ "W", "2", "W", "W", "W", "W", "m", "W" ],
  [ "W", " ", "W", " ", "3", " ", " ", "W" ],
  [ "W", " ", "W", "8", " ", "W", " ", "W" ],
  [ "W", " ", "W", "W", "m", "W", "5", "W" ],
  [ "W", "1", " ", " ", " ", "m", " ", "W" ],
  [ "W", "W", "W", "E", "W", "W", "W", "W" ]
]

path = [ (0, 2), (1, 2), (2, 2), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (8, 3) ]

"""


def find(maze):

    path = []
    visited = set()
    deltas = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    have_seen_monster = False

    def dfs(row, col):
        nonlocal have_seen_monster

        if row < 0 or col < 0 or row >= len(maze) or col >= len(maze[0]):
            return False

        if (row, col) in visited or maze[row][col] == 'W':
            return False

        if maze[row][col] == 'm':
            if have_seen_monster:
                return False
            else:
                have_seen_monster = True

        if maze[row][col] == 'E':
            path.append([row, col])
            return True

        visited.add((row, col))
        path.append([row, col])
        for delta in deltas:
            res = dfs(row + delta[0], col + delta[1])
            if res:
                return res
        visited.remove((row, col))
        path.pop()

        return False

    for x in range(len(maze)):
        for y in range(len(maze[0])):
            if maze[x][y] == 'S':
                dfs(x, y)

    return path


maze = [
    ["W", "W", "S", "W", "W", "W", "W", "W"],
    ["W", " ", " ", "W", " ", " ", " ", "W"],
    ["W", " ", " ", " ", " ", "W", " ", "W"],
    ["W", "2", "W", "W", "W", "W", "m", "W"],
    ["W", " ", "W", " ", "3", " ", " ", "W"],
    ["W", " ", "W", "8", " ", "W", " ", "W"],
    ["W", " ", "W", "W", "m", "W", "5", "W"],
    ["W", "1", " ", " ", " ", "m", " ", "W"],
    ["W", "W", "W", "E", "W", "W", "W", "W"]
]

print(find(maze))
