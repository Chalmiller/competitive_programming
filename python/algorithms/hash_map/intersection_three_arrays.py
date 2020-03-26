# 1213: Intersection of Three Sorted Arrays
from typing import *

class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        # Iterative
        for num in arr1:
            if num in arr2 and num in arr3:
                yield num

obj = Solution()
intersect = obj.arraysIntersection([1,2,3,4,5], [1,2,5,7,9], [1,3,4,5,8])
print(intersect)