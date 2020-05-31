from typing import *
import collections

class Solution:
  def minSteps(self, s: str, t: str) -> int:
    if s == t:
      return 0
    if set(t) == set(s):
      return 0

    s_counter = collections.Counter(s)
    t_counter = collections.Counter(t)

    diff = dict(s_counter - t_counter)
    count = 0
    for k, v in diff.items():
      count += v


    
obj = Solution()
print(obj.minSteps("friend", "family"))

        