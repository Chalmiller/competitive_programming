from typing import *

class Solution:
    def climbStairs(self, n: int) -> int:
        def count_stairs(memo, n):

          if n == 0:
            return 1
          if n == 1:
            return 1
          if n == 2:
            return 2

          if dp[n] == 0:

            first_step = count_stairs(memo, n-1)
            second_step = count_stairs(memo, n-2)
            dp[n] = first_step + second_step

          return dp[n]
        
        dp = [0 for _ in range(n + 1)]
        print(dp)
        return count_stairs(dp, n)

obj = Solution()
print(obj.climbStairs(5))