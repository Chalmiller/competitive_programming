from typing import *

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
      # if numRows == 0:
      #   return []
      # res = [[1]]
      # for i in range(numRows - 1):
      #   prev = res[-1]
      #   curr_level = []
      #   curr_level.append(1)
      #   for i in range(len(prev)-1):
      #     curr_level.append(prev[i] + prev[i + 1])
      #   curr_level.append(1)
      #   res.append(curr_level)
      # return res

      triangle = []

      for row_num in range(numRows):
          # The first and last row elements are always 1.
          row = [None for _ in range(row_num+1)]
          print(row)
          row[0], row[-1] = 1, 1

          # Each triangle element is equal to the sum of the elements
          # above-and-to-the-left and above-and-to-the-right.
          for j in range(1, len(row)-1):
              row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]

          triangle.append(row)

      return triangle
          

obj = Solution()
print(obj.generate(5))
