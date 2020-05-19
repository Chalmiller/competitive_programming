from typing import *
import itertools

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name_group = [(k, g) for k, g in itertools.groupby(name)]
        typed_group = [(k, g) for k, g in itertools.groupby(typed)]

        if len(name_group) != len(typed_group):
          return False

        return all([let1 == let2 and count1 <= count2 for (let1, count1), (let2, count2) in zip(name_group, typed_group)])

obj = Solution()
print(obj.isLongPressedName("alex",
"aaleelx"))