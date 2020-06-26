from typing import *

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    profit = 0

    for i in range(len(prices)-1):
      curr_max = max(prices[i+1:]) - prices[i]
      if curr_max >= 0:
        profit = max(curr_max, profit)
    return profit