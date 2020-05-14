from typing import *
import copy

class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        
        continue_changing = True
        
        while continue_changing:
          new_array = copy.copy(arr)
          for i in range(1, len(arr) - 1):
            if arr[i - 1] > arr[i] and arr[i + 1] > arr[i]:
              arr[i] += 1
            elif arr[i - 1] < arr[i] and arr[i + 1] < arr[i]:
              arr[i] -= 1
          continue_changing = not(arr == new_array)
        return arr

obj = Solution()
print(obj.transformArray([1,6,3,4,3,5]))