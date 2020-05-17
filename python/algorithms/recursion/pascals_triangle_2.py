from typing import *

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
      
        if rowIndex == 0:
          return [1]
        else:
          line = [1]

          prev = self.getRow(rowIndex - 1)
          for i in range(len(prev) -1):
            line.append(prev[i] + prev[i + 1])

          line += [1]
        return line

obj = Solution()
print(obj.getRow(5))