class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        deltas = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def is_out(row, col):
            return row < 0 or col < 0 or row >= len(board) or col >= len(board[0])

        def is_exist(row, col, start):

            if start == len(word):
                return True

            if is_out(row, col) or board[row][col] == '#' or board[row][col] != word[start]:
                return False

            temp = board[row][col]
            board[row][col] = '#'
            for delta in deltas:
                if is_exist(row + delta[0], col + delta[1], start + 1):
                    return True
            board[row][col] = temp

        for row in range(len(board)):
            for col in range(len(board[0])):
                if is_exist(row, col, 0):
                    return True

        return False
