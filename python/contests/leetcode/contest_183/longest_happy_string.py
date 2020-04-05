from typing import *
from collections import Counter
from itertools import permutations

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        let_count = Counter(a=a, b=b, c=c)
        # string_list = []
        # perm = permutations(let_count.elements())
        # for i in perm:
        #     potential = "".join(i)
        #     if 'aaa' or 'bbb' or 'ccc' in potential:
        #         continue
        #     else:
        #         return potential
        total_tries = a + b + c
        for let in range(total_tries)


obj = Solution()
let = obj.longestDiverseString(1,1,7)
print(let)