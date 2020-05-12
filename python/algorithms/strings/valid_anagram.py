from typing import *
import collections

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      if len(collections.Counter(t) - collections.Counter(s)) == 0 and len(collections.Counter(s) - collections.Counter(t)) == 0:
        return True 
      else:
        return False

obj = Solution()
print(obj.isAnagram('a', 'ab'))