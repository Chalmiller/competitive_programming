from typing import *
import heapq

class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        heapq.heapify(A)

        for _ in range(K):
          low_conversion = heapq.heappop(A)
          heapq.heappush(A, -low_conversion)
        return sum(A)

obj = Solution()
print(obj.largestSumAfterKNegations([2,-3,-1,5,-4], 2))
