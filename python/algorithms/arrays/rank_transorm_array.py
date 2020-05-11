from typing import *

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_array = sorted(arr)
        rank_dict = {}
        res = []
        it = 0
        index = 0
        while it < len(sorted_array):
          if sorted_array[it] not in rank_dict:
            rank_dict[sorted_array[it]] = index + 1
            index += 1
          it += 1
        for num in arr:
          res.append(rank_dict[num])
        return res

obj = Solution()
print(obj.arrayRankTransform([37,12,28,9,100,56,80,5,12]))