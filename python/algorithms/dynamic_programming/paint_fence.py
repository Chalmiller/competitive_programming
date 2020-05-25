from typing import *

class Solution(object):
    def numWays(self, n, k):
      if n == 0:
        return 0
      elif n == 1:
        return k
      elif n == 2:
        return k**k

      first = k
      second = k**k

      for i in range(3, n+1):
        third = first*(k-1) + second*(k-1)
        first, second = second, third

      return third