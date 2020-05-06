from typing import *

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix) - 1):
          for j in range(len(matrix[0]) - 1):
            if matrix[i][j] != matrix[i+1][j+1]:
              return False
        return True


obj = Solution()
print(obj.isToeplitzMatrix([
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]))
