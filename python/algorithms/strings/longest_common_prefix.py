from typing import *

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        for i, c in enumerate(zip(*strs)): 
            if len(set(c)) > 1: return strs[0][:i]
        return min(strs)

obj = Solution()
print(obj.longestCommonPrefix(["dog","racecar","car"]))
