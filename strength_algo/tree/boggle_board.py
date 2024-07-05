''' 
▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
✏️ Description
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Q. Boggle is played on a 4x4 grid. Each square on the grid has a letter. The goal is to make as many words as possible by starting anywhere on the board and the moving to any adjacent letters in the grid (horizontally, vertically or diagonally). Given a 4x4 grid and an array containing all valid words, implement an algorithm that returns all the valid words that can be found in the grid.

Examples:
• Given a board:
  [
    'COPS',
    'EDXZ',
    'RLQU',
    'BOKI'
 ]
• And words ['CODE', 'CODER', 'MISSING']
Return ['CODE', 'CODER'] (order does not matter)
▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
🟦 Python
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
def findWords(board: list[list[str]], words: list[str]) -> list[str]:
    # Write your code here.
    pass

# Test Cases
print(findWords(['COPS', 'EDXZ', 'RLQU', 'BOKI'], ['CODE', 'CODER', 'MISSING'])) # ['CODE', 'CODER'] (order does not matter)

1. Explore/Brainstorm
  1. iterating over the words - find each word in the board
      -> explore in all directions - dfs
      - if found - add to the res
      -> if not find move on to next word
  
  <Comeback to it>
  
  runtime: for each word -> O(n!) where n is length of word
  and O(n!)* m where m is length of words array. 

  space: - O(n) where n is length of each word
  
2. Test cases
3. Plan
    
   iterate over words array(0...len(words)):
     - for each word:
        find(word)
        if find returns true:
            add the word to the result array

    - find function takes the word as the input and the board
        iterate the board and do dfs at each charater to see if there is match:
            if there is a match, return True, else return False

    - dfs function taks the index of the word and the index of the board
        dfs(x, y, index)
        check if the charater at x and y:
            if the x and y are out of boardary, return False
            or if the x and y are in visited, return False
            or if the charateor at x and y are not equal to the word[index], return False
            add the x and y in visited
            do a 4 directions iteration of the neighbors
                res = dfs(x + delta, y+delta, index+1)
                if res is True, return True
            remove x and y from visited
            else
                return False
4. Implementation

'''
'''
Time complexity: O(M(4⋅3 ^L−1)
 )), where M is the number of cells in the board and L is the maximum length of words.

It is tricky is calculate the exact number of steps that a backtracking algorithm would perform. We provide a upper bound of steps for the worst scenario for this problem. The algorithm loops over all the cells in the board, therefore we have M as a factor in the complexity formula. It then boils down to the maximum number of steps we would need for each starting cell (i.e.4⋅3 
L−1
 ).

Assume the maximum length of word is L, starting from a cell, initially we would have at most 4 directions to explore. Assume each direction is valid (i.e. worst case), during the following exploration, we have at most 3 neighbor cells (excluding the cell where we come from) to explore. As a result, we would traverse at most 4⋅3 
L−1
  cells during the backtracking exploration.

One might wonder what the worst case scenario looks like. Well, here is an example. Imagine, each of the cells in the board contains the letter a, and the word dictionary contains a single word ['aaaa']. Voila. This is one of the worst scenarios that the algorithm would encounter.
'''

def findWords(board: list[list[str]], words: list[str]) -> list[str]:

    found = []
    deltas = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def out_of_bound(row, col):
        return row < 0 or col < 0 or row >= len(board) or col >= len(board[0])

    def dfs(row, col, word, index, visited):
        if index == len(word):
            return True
        if out_of_bound(row, col) or (row, col) in visited or board[row][col] != word[index]:
            return False
        visited.add((row, col))
        for delta in deltas:
            res = dfs(row + delta[0], col + delta[1], word, index + 1, visited)
            if res:
                return True
        visited.remove((row, col))
        return False

    def findWord(word):
        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(row, col, word, 0, set()):
                    return True
        return False

    for word in words:
        if findWord(word):
            found.append(word)

    return found


print(findWords(['COPS', 'EDXZ', 'RLQU', 'BOKI'],
      ['CODE', 'CODER', 'MISSING']))
