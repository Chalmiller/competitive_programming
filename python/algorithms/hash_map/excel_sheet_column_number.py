from typing import *

class Solution:
    def titleToNumber(self, s: str) -> int:
      col = 0
      for i in range(len(s)):
        col += (ord(s[i]) - 64) * 26**((len(s) - (i+1)))
      return col



obj = Solution()
print(obj.titleToNumber("ABA"))