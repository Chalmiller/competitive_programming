from typing import *

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        invert = list(zip(*board))

        # row_wise comparisons
        for row in range(len(board)):
          cache = set()
          for col in range(len(board[row])):
            val = board[row][col]
            if val in cache:
              return False
            else:
              cache.add(val)
        
        for row in range(len(invert)):
          cache = set()
          for col in range(len(invert[row])):
            val = invert[row][col]
            if val in cache:
              return False
            else:
              cache.add(val)

        return True
        
obj = Solution()
print(obj.isValidSudoku([
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]))
