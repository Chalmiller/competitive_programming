from typing import *
import math

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
      a = min(start, destination)
      b = max(start, destination)
      print(distance[a:b], distance)
      return min(sum(distance[a:b]), sum(distance) - sum(distance[a:b]))

obj = Solution()
print(obj.distanceBetweenBusStops([3,6,7,2,9,10,7,16,11], 6, 2))
