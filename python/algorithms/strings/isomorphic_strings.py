from typing import *

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
          if s[i] not in s_dict:
            s_dict[s[i]] = t[i]
          elif s_dict[s[i]] != t_dict[t[i]]:
            return False
          if t[i] not in t_dict:
            t_dict[t[i]] = s[i]
          elif t_dict[t[i]] != s_dict[s[i]]:
            return False
        return True