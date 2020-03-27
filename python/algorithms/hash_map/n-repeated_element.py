from typing import *
from collections import Counter

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        counter = Counter()
        new_set = set()
        for num in A:
            counter[num] += 1

        for el,k in dict(counter):
            if k in new_set:
                return False
            else:
                new_set.add(k)
                
        return True
        