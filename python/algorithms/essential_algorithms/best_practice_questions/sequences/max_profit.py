from typing import *
import math

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    max_profit = 0

    # [7,6,4,3,1]
    # 
    for i in range(len(prices) - 1):
      curr_max = max(prices[i+1:]) - prices[i]
      if curr_max >= 0:
        max_profit = max(max_profit, curr_max)
    return max_profit

obj = Solution()
print(obj.maxProfit([7,6,4,3,1]))
           