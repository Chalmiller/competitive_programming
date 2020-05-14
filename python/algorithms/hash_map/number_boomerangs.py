from typing import *
import collections
import math

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0
        for x in points:
            hashmap = collections.defaultdict(int)
            for y in points:
                dist = pow(x[0] - y[0], 2) + pow(x[1] - y[1], 2)
                hashmap[dist] += 1
            for key in hashmap:
                res += hashmap[key] * (hashmap[key] - 1)
        return res

obj = Solution()
print(obj.numberOfBoomerangs([[0,0],[1,0],[2,0]]))