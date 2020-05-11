from typing import *
import collections

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        num_count = collections.Counter(arr)
        quarter_array = len(arr)//4
        for el, count in num_count.items():
          if count > quarter_array:
            return el

obj = Solution()
print(obj.findSpecialInteger([1,2,2,6,6,6,6,7,10]))
        