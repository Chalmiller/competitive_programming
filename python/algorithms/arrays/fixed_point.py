# 1064: Fixed Point
from typing import *

class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        # Brute Force
        for index, num in enumerate(A):
            if num == index:
                return num
        return -1
        """
        Binary Search Method

        l, r = 0, len(A) - 1
        while l < r:
            m = (l + r) / 2
            if A[m] - m < 0:
                l = m + 1
            else:
                r = m
        return l if A[l] == l else -1
        """