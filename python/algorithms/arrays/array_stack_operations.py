from typing import *

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
      operations = []
      build_array = []
      for num in range(1, n + 1):
        if num in target:
          build_array.append(num)
          operations.append("Push")
        elif num not in target:
          operations.extend(["Push", "Pop"])
        
        if build_array == target:
          return operations

obj = Solution()
print(obj.buildArray([2,3,4], 4))
