from typing import *

class Solution:
    def calPoints(self, ops: List[str]) -> int:
      curr_sum = 0
      index1 = 0
      index2 = 0
      while index2 < len(ops):
        if ops[index2] == "C":
          ops = ops[:index2-1] + ops[index2+1:]
          index2 = 0
        elif ops[index2] == "D":
          ops[index2] = int(ops[index2 - 1]) * 2
          index2 = 0
        elif ops[index2] == "+":
          ops[index2] = int(ops[index2 - 1]) + int(ops[index2 - 2])
          index2 = 0
        else:
          ops[index2] = int(ops[index2])
          index2 += 1
      return sum(ops)

obj = Solution()
print(obj.calPoints(["5","2","C","D","+"]))
