# Group Anagram
from typing import *

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for w in strs:
            key = tuple(sorted(w))
            d[key] = d.get(key, []) + [w]
            print(d.get(key, []))
        return list(d.values())

obj = Solution()
listy = obj.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(listy)