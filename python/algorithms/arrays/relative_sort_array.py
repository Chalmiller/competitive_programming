# 1122: Relative Sort Array
from typing import *

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        compiled_list = []
        for num in arr2:
            while num in arr1:
                index = arr1.index(num)
                compiled_list.append(arr1.pop(index))
        arr1.sort()
        compiled_list.extend(arr1)
        return compiled_list

obj = Solution()
num_list = obj.relativeSortArray([2,3,1,3,2,4,6,7,9,2,44,17], [2,1,4,3,9,6])
print(num_list)