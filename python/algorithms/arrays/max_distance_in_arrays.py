from typing import *

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        
        min_ = arrays[0][0]
        max_ = arrays[0][-1]
        
        
        res = 0
        for lst in range(1,len(arrays)):
            res = max(res,max(abs(arrays[lst][0]-max_),abs(arrays[lst][-1]-min_)))
            min_ = min(min_,arrays[lst][0])
            max_ = max(max_,arrays[lst][-1])
            
        return res

obj = Solution()
print(obj.maxDistance([[1,2,3],[4,5],[1,2,3]]))
