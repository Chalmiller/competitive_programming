from typing import *

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_map = {}

        for index, value in enumerate(nums):
          if hash_map.get(value, -1) >= 0:
            diff = index - hash_map[value]
            if diff <= k:
              return True
          hash_map[value] = index
          print(hash_map)
        return False
      
obj = Solution()
print(obj.containsNearbyDuplicate([1,2,3,1,2,3], 2))