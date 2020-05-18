from typing import *
import math
import heapq

class Solution:
  def maximumProduct(self, nums: List[int]) -> int:
    minHeap = []
    for num in nums:
      heapq.heappush(minHeap, num)
    two_smallest = [heapq.heappop(minHeap) for _ in range(2)]
    maxHeap = []
    for num in nums:
      heapq.heappush(maxHeap, -num)
    three_largest = [-heapq.heappop(maxHeap) for _ in range(3)]
    three_largest.sort()
    two_smallest.sort()
    return max(two_smallest[0] * two_smallest[1] * three_largest[-1], three_largest[0] * three_largest[1] * three_largest[2])

obj = Solution()
print(obj.maximumProduct([-4,-3,-2,-1,60]))