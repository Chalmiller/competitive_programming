from typing import *

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = {}
        t_counter = {}

        if len(s) != len(t):
          return False

        for i in range(len(s)):
          s_counter[s[i]] = s_counter.get(s[i], 0) + 1
          t_counter[t[i]] = t_counter.get(t[i], 0) + 1
        
        return s_counter == t_counter

obj = Solution()
print(obj.isAnagram("anagrama", "nagaram"))