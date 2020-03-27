# 973: K Closest Points to Origin
from typing import *
from collections import defaultdict
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # Brute Force
        # res_list = []
        # eucl_dist = dict()
        # for index, loc in enumerate(points):
        #     eucl_dist[index] = loc[0]**2 + loc[1]**2
        # new_dict = list({k: v for k, v in sorted(eucl_dist.items(), key = lambda item: item[1])})
        # for i in range(K):
        #     res_list.append(points[new_dict[i]])
        # return res_list

        # Heap solution
        return heapq.nsmallest(K, points, lambda x, y: x*x + y*y)

obj = Solution()
res = obj.kClosest([[3,3],[5,-1],[-2,4]], 2)
print(res)
