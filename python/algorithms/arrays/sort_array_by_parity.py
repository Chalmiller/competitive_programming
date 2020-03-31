# 905: Sort Array by Parity
from typing import *

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        res = [num for num in A if num%2 == 0].extend([num for num in A if num%2 == 1])
        return res