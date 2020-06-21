from typing import *

class Solution:
  def singleNumber(self, nums: List[int]) -> int:
    cache = {}

    for num in nums:
      cache[num] = cache.get(num, 0) + 1
    
    sorted_cache = sorted(cache.items(), key=lambda kv: (kv[1], kv[0]))
    return sorted_cache[0][0]

obj = Solution()
print(obj.singleNumber([4,1,2,1,2]))