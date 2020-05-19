from typing import *
import collections

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = collections.Counter(text)
        cntBalloon = collections.Counter('balloon')
        return min([cnt[c]//cntBalloon[c] for c in cntBalloon])

obj = Solution()
print(obj.maxNumberOfBalloons("loonbalxballpoon"))
            
