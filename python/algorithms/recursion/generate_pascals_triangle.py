from typing import *

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
      if numRows == 0:
        return []
      res = [[1]]
      for i in range(numRows - 1):
        prev = res[-1]
        curr_level = []
        curr_level.append(1)
        for i in range(len(prev)-1):
          curr_level.append(prev[i] + prev[i + 1])
        curr_level.append(1)
        res.append(curr_level)
      return res
          

obj = Solution()
print(obj.generate(5))
