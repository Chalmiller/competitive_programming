# 942: DI String Match
from typing import *
from itertools import permutations

class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        valid_list = []
        num_list = [i for i in range(len(S)+1)]
        perm_list = permutations(num_list)
        for perm in perm_list:
            valid_list.extend([perm if all([True if (S[index] == "I" and (perm[index] > perm[index-1])) or (S[index] == "D" and (perm[index] < perm[index-1])) else False for index in range (1, len((perm)))])
        return valid_list
                
        
