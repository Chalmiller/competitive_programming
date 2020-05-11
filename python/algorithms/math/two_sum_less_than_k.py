from typing import *
import math

class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        _max = -math.inf
        cache = {}

        for i in range(len(A) - 2):
          for j in range(i + 1, len(A)):
            if A[i] + A[j] < K:
              _max = max(_max, A[i] + A[j])

        return (_max if _max > 0 else -1)
  
obj = Solution()
print(obj.twoSumLessThanK([803,468,292,154,924,424,197,277,753,86,984,144,105,450,287,265,655,404,407,794,513,976,241,272,84,503,65,654,805,413,362,907,297,473,113,567,646,607,806,674,424,753,870,574,765,170,603,696,513,58],
300))