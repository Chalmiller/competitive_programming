from typing import *
import unittest

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Task: Modify the matrix in place to be zero if there is a zero found within the arrays
        Intuition: I can handle this functionally. 

        Algorithm:
            - iterate through the matrix
                - if the value at i is a zero feed the function the array and modify in place
            - return the modified array
        """
        def modify_array(row, col, arr):
            # Modify the respective row
            for c in range(len(arr[0])):
                arr[row][c] = 0
            
            # modify the respective column
            for r in range(len(arr)):
                arr[r][col] = 0

            return arr

        # null check
        if not matrix: return []
        index_cache = []

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    index_cache.append([r,c])
                    
        for r, c in index_cache:
            matrix = modify_array(r, c, matrix)
            
        return matrix



class TestSetZeros(unittest.TestCase):

    def test_set_zeros(self):
        input = [[1,1,1],[1,0,1],[1,1,1]]
        output = [[1,0,1],[0,0,0],[1,0,1]]
        self.assertEqual(output, Solution().setZeroes(input))

unittest.main(verbosity=2)
