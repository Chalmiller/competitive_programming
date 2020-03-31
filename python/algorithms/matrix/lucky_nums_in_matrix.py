# 1380: Lucky Numbers in a Matrix
from typing import *

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        luck_nums = []
        row_min = [min(row) for row in matrix]
        max_col = [luck_nums.append(max(col)) for col in zip(*matrix) if max(col) in row_min]
        return luck_nums


obj = Solution()
num = obj.luckyNumbers([[1,10,4,2],[9,3,8,7],[15,16,17,12]])
print(num)