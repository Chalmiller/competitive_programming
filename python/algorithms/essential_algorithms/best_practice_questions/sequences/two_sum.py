from typing import *
import collections

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    cache = collections.defaultdict(list)
    # [3,2,4], 6
    for index, num in enumerate(nums):
      needed = target - num
      if needed in cache:
        return [cache[needed][0], index]
      else:
        cache[num].append(index)
    


obj = Solution()
print(obj.twoSum([3,2,4], 6))
