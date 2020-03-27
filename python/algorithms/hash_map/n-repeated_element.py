from typing import *
from collections import Counter

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        counter = Counter()
        for num in A:
            counter[num] += 1
        return counter.most_common(1)[0][0]
        