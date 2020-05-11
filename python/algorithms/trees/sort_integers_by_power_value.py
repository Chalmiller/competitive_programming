from typing import *

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def power_value(num):
          count = 0
          while num != 1:
            if num % 2 == 0:
              num /= 2
            else:
              num = num * 3 + 1
            count += 1
          return count
        
        power_values = {}
        
        for num in range(lo, hi + 1):
          power_values[num] = power_values.get(num, power_value(num))

        res = sorted(power_values.items(), key = lambda kv: kv[1])
        return res[k-1][0]

        

obj = Solution()
print(obj.getKth(12, 15, 2))



