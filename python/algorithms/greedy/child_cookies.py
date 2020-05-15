from typing import *

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        content_children = 0
        cookies_available = 0

        while cookies_available < len(s) and content_children < len(g):
          if s[cookies_available] >= g[content_children]:
            content_children += 1
          cookies_available += 1
        return content_children

obj = Solution()
print(obj.findContentChildren([1,2], [1,2,3]))