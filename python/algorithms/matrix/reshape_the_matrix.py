from typing import *
import itertools

class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(nums) * len(nums[0]):
          return nums
        it = itertools.chain(*nums)
        return [list(itertools.islice(it, c)) for _ in range(r)]

obj = Solution()
print(obj.matrixReshape([[1,2],
 [3,4]], 1, 4))

