from typing import *

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = set()
        for word in words:
          for i in range(len(words)):
            if word == words[i]:
              continue
            else:
              if words[i].find(word) != -1:
                res.add(word)
        return list(res)

obj = Solution()
print(obj.stringMatching(["leetcoder","leetcode","od","hamlet","am"]))