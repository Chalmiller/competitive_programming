from typing import *

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = [False] * len(candies)
        max_candies = max(candies)
        for index in range(len(candies)):
          if candies[index] + extraCandies >= max_candies:
            result[index] = True
        return result