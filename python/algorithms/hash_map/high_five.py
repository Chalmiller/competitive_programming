# 1086: High Five
from typing import *
from collections import defaultdict
import heapq
import bisect

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:

        # using defaultdict and a heapq
        # d = defaultdict(list)
        # for id_, score in items:
        #     d[id_].append(score)
        # ans = []
        # for k in d:
        #     ans.append([k, sum(heapq.nlargest(5, d[k]))//5])
        # return ans

        D = defaultdict(list)
        for student, score in items:
            bisect.insort(D[student], score)
        return [[student, sum(D[student][-5:])//5] for student in D]


obj = Solution()
num = obj.highFive([[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]])
print(num)