from typing import *
import collections

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        c = collections.Counter((A + " " + B).split())
        print(c)
        return [w for w in c if c[w] == 1]

obj = Solution()
print(obj.uncommonFromSentences("s z z z s", "s z ejt"))
        