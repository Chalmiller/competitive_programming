# 728: Self Dividing Numbers
from typing import *

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        num_list = []
        for i in range(left, right+1):
            if all([True if (int(j) != 0) and (i%int(j) == 0) else False for j in str(i)]):
                num_list.append(i) 
        return num_list
                
                    
            