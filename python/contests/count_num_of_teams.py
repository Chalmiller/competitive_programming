# 5369: Count Number of Teams
from typing import *
import itertools

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        permutations = itertools.combinations(rating, 3)
        valid_perms = []

        for perm in permutations:
            min_perm = min(perm)
            max_perm = max(perm)
            if perm.index(min_perm) == 0 and perm.index(max_perm) == 2:
                valid_perms.append(perm)
            elif perm.index(min_perm) == 2 and perm.index(max_perm) == 0:
                valid_perms.append(perm)
            else:
                continue
        
        return len(valid_perms)

obj = Solution()
num = obj.numTeams([2,5,3,4,1])
print(num)
