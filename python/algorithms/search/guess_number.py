from typing import *

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        start, end = 1, n

        while start < end:
          mid = start + (end - start)//2

          if guess(mid) == 1:
            start = mid + 1
          elif guess(mid) == -1:
            end = mid
          else:
            return mid
        return start