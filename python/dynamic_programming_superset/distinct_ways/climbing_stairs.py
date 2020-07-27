import unittest
from typing import *

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
          return n

        s = 2
        p = 1

        for _ in range(3, n+1):
          p = s + p
          s, p = p, s
        return s