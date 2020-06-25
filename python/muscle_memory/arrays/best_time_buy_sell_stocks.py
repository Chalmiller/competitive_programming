from typing import *

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Task: Determine the best time to buy and sell. Multiple transactions can occur
        Intuition: I've seen this as a greedy algorithm before so I can start there

        Algorithm:
          1. Greedily take each min and sell once a bigger value is found
          2. 
        """
        _max_profit = 0

        for i in range(1, len(prices)):
          if prices[i] > prices[i-1]:
            _max_profit += prices[i] - prices[i-1]
        return _max_profit
