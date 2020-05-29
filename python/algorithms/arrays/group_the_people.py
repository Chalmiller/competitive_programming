from typing import *
import collections

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groupings = collections.defaultdict(list)

        for i, group in enumerate(groupSizes):
          groupings[group].append(i)

        res = []
        for key in groupings.keys():
          for j in range(0, len(groupings[key]), key):
            res.append(groupings[key][j:j+key])


obj = Solution()
print(obj.groupThePeople([2,1,3,3,3,2]))
