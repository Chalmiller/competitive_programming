from typing import *

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if coordinates[1][0] - coordinates[0][0] == 0:
          return False
        slope = (coordinates[1][1] - coordinates[0][1]) // (coordinates[1][0] - coordinates[0][0])
        for i in range(1, len(coordinates) - 1):
          if coordinates[i + 1][0] - coordinates[i][0] == 0:
            return False
          new_slope = (coordinates[i+1][1] - coordinates[i][1]) // (coordinates[i + 1][0] - coordinates[i][0])
          if new_slope != slope:
            return False
        return True

obj = Solution()
print(obj.checkStraightLine([[-7,-3],[-7,-1],[-2,-2],[0,-8],[2,-2],[5,-6],[5,-5],[1,7]]))
          