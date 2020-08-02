from typing import *
import unittest

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Task: Crossword puzzle solver
        Intuition: Backtracking algorithm again

        Algorithm:
            - build strings with backtracking algorithm
            - if the string is equal to the desired word, return true
            - else: return false

            General backtracking algorithm:
                - create a solution matrix filled with 0s
                - create a recursive function, which takes initial matrix, output matrix and position of (i, j)
                - if the position is out of the matrix or the position is not valid then return
                - mark the position output[i][j] as 1 and check if the current position is destination or not. If destination is reached print the output 
                    matrix and return
                - Recursively call for position (i+1, j) and (i, j+1)
                - Unmark position (i, j) i.e. output[i][j] = 0
        """
        self.ROWS = len(board)
        self. COLS = len(board[0])
        self.board = board

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.backtrack(row, col, word):
                    return True
        return False


    def backtrack(self, row, col, suffix):
        if len(suffix) == 0:
            return True

        if row < 0 or row == self.ROWS or col < 0 or col == self.COLS or self.board[row][col] != suffix[0]:
            return False

        ret = False
        self.board[row][col] = '#'

        for row_offset, col_offset in [(0,1), (1,0), (0,-1), (-1,0)]:
            ret = self.backtrack(row+row_offset, col + col_offset, suffix[1:])
            if ret: break
        
        self.board[row][col] = suffix[0]
        return ret


class TestExist(unittest.TestCase):

    def test_working_exist(self):
        pass

unittest.main(verbosity=2)    

    