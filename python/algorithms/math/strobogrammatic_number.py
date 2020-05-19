from typing import *

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
      print(list(zip(num, num[::-1])))
      return all(c + d in '696 00 11 88' for c, d in zip(num, num[::-1]))

obj = Solution()
print(obj.isStrobogrammatic("69"))