# 1337: The K weakest Row in a Matrix
from typing import *

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        mat_rating = dict()
        for i in range(len(mat)):
            mat_rating[i] = sum(mat[i])
        sort_mat_rating = {k: v for k,v in sorted(mat_rating.items(), key= lambda item: item[1])}
        weakest_rows = [key for key in sort_mat_rating.keys()]
        return weakest_rows[:k]
        
