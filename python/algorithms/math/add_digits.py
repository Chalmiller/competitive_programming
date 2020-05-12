from typing import *

class Solution:
    def addDigits(self, num: int) -> int:
        num_string = str(num)

        while len(num_string) != 1:
          num_list = [int(num) for num in num_string]
          num_string = str(sum(num_list))
        return int(num_string)

obj = Solution()
print(obj.addDigits(38))

