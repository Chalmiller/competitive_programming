from typing import *
import math

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
      Aindex = {u: i for i, u in enumerate(list1)}
      best, ans = 1e9, []

      for j, v in enumerate(list2):
        i = Aindex.get(v, 1e9)
        if i + j < best:
          best = i + j
          ans = [v]
        elif i + j == best:
          ans.append(v)
      return ans

obj = Solution()
print(obj.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]))

