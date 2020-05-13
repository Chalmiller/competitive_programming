from typing import *
import math

class Solution:
    def maxScore(self, s: str) -> int:
      _max = -math.inf
      for i in range(1, len(s)):
        left = s[:i]
        right = s[i:]
        _max = max((left.count('0') + right.count('1')), _max)
      return _max

obj = Solution()
print(obj.maxScore("1111"))