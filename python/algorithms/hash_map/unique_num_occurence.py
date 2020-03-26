# 1207: unique Number of Ocurrences
from typing import *
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter()
        new_set = set()
        for num in arr:
            counter[num] += 1

        for el,k in counter.items():
            if k in new_set:
                return False
            else:
                new_set.add(k)
                
        return True

obj = Solution()
num = obj.uniqueOccurrences([1,2,2,1,1,3])
print(num)