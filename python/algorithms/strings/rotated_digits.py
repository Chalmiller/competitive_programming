from typing import *

class Solution:
    def rotatedDigits(self, N: int) -> int:
        ans = 0
        for num in range(1, N + 1):
          num_string = str(num)
          print(num_string)

          ans += (all(d not in '13478' for d in num_string) \
                  and any(d in '2569' for d in num_string))
        return ans

obj = Solution()

print(obj.rotatedDigits(2))