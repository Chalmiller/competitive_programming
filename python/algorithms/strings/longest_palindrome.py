from typing import *
import collections
import copy
import math

class Solution:
    def longestPalindrome(self, s):
      ans = 0
      for v in collections.Counter(s).values():
          ans += v // 2 * 2
          print(ans, v)
          if ans % 2 == 0 and v % 2 == 1:
              ans += 1
      return ans

obj = Solution()
print(obj.longestPalindrome("abccccdd"))
      