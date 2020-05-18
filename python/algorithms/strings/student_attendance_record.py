from typing import *

class Solution:
    def checkRecord(self, s: str) -> bool:
        count_A = s.count('A')
        if count_A > 1:
          return False
        # Sliding window approach
        start = 0
        end = 3
        while end <= len(s):
          count_L = s[start:end].count('L')
          if count_L > 2:
            return False
          start += 1
          end += 1
        return True

obj = Solution()
print(obj.checkRecord("PPALLL"))