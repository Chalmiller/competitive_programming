from typing import *

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {c: i for i, c in enumerate(S)}
        print(last)
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
          j = max(j, last[c])
          print(i, j, c)
          if i == j:
            ans.append(i - anchor + 1)
            anchor = i + 1

        return ans

obj = Solution()
print(obj.partitionLabels("ababcbacadefegdehijhklij"))