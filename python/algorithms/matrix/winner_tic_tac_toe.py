from typing import *

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        def is_win(grid):
          # Check a column win
          col_list = zip(*grid)
          print(list(col_list))
          for col in list(col_list):
            el = col[0]
            for mark in col:
              if mark != el:
                return False
          # Check a row win
          for row in grid:
            if row[0] != " " and all(row):
              return True
          # Check a diagonal win
          fdiag = []
          row, col = 0, 0 
          while row < len(grid):
            fdiag.append(grid[row][col])
            row += 1
            col += 1

          col = 0
          bdiag = []
          while row > -1:
            bdiag.append(grid[row-1][col])
            row -= 1
            col += 1

          print(fdiag, bdiag)

        print(is_win([['X','X','O'],['O',"O","X"],['X','O','X']]))

obj = Solution()
print(obj.tictactoe([]))

            
          