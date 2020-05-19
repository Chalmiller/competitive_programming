from typing import *
import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        _max_profit = -math.inf
        _min = math.inf
        for price in prices:
          if price < _min:
            _min = price
          else:
            _max_profit = max(_max_profit, price - _min) 
        return _max_profit if _max_profit > -math.inf else 0


obj = Solution()
print(obj.maxProfit([3,2,6,5,0,3]))
print(obj.maxProfit([7,1,5,3,6,4]))

        
