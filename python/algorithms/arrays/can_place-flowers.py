from typing import *
import itertools

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]

        cur = 0
        res = 0

        for i in range(len(flowerbed)):
          if flowerbed[i] == 0:
            cur += 1
          if flowerbed[i] == 1 or i == len(flowerbed) - 1:
            res += (cur - 1) // 2
            cur = 0
          
        return res >= n