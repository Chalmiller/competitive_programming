from typing import *

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
      for direction, amount in shift:
        if direction == 0:
          shift_left = s[amount:] + s[:amount]
          s = shift_left
        else:
          shift_right = s[-amount:] + s[:-amount]
          shift_right
          s = shift_right
        
      return s

obj = Solution()
ans = obj.stringShift("abc", [[0,1],[1,2]])
print(ans)