from typing import *

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
      index = 1
      while index < num//2:
        square = index * index
        if square == num:
          return True
        else:
          index += 1
      return False
