from typing import *
import collections

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        a=list(range(1,len(nums)+1))
        miss=sum(set(a))-sum(set(nums))
        dup=sum(nums)-sum(set(nums))
        return[dup,miss]

obj = Solution()
print(obj.findErrorNums([2,2]))

