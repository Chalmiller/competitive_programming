from typing import *

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [0] * (amount + 1)

        for coin in coins:
          for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[amount] if dp[amount] != 0 else -1

