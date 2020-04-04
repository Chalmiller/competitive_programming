# 1002: Find Common Character
from typing import *
from collections import Counter

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        res = Counter(A[0])
        for a in A:
            print(res)
            res &= Counter(a)
            print(list(res), list(res.elements()))
        return list(res.elements())
        

            

obj = Solution()
lists = obj.commonChars(["bella","label","roller"])
print(lists)