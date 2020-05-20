from itertools import chain, islice
from typing import Iterator

class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        
        s_list = [x.upper() for x in S if x!='-']
        n = len(s_list)
        groups = n//K
        rem_ele  = n%K
        final_list = []
        if rem_ele!=0:
            final_list.append("".join(x for x in s_list[:rem_ele]))
        for i in range(groups):
            final_list.append("".join(x for x in s_list[rem_ele:rem_ele+K]))
            
            rem_ele = rem_ele + K
        return "-".join(x for x in final_list)


obj = Solution()
print(obj.licenseKeyFormatting("2-5g-3-J", 2))