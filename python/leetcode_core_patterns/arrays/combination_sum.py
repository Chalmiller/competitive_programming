from copy import copy
from typing import *

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        if len(candidates) == 0: return res
        candidates.sort()

        def solve(c, ind, t, path):
          if t < 0: return
          if t == 0:
            res.append(path.copy())
            return
          
          for i in range(ind, len(c)):
            path.append(c[i])
            solve(c, i, t-c[i], path)
            path.pop()

        solve(candidates, 0, target, [])
        return res