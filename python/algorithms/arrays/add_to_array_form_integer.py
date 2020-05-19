from typing import *

class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        str_list = list(map(lambda x:str(x), A))
        int_form = int("".join(str_list)) + K
        
        output_list = [int(num) for num in str(int_form)]
        return output_list



obj = Solution()
print(obj.addToArrayForm([1,2,0,0], 34))