# 977: Squares of a Sorted Array
from typing import *

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(map(lambda a: a*a, A))