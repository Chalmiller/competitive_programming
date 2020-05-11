from typing import *

class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
      res = []
      for word in words:
        index1 = 0
        index2 = len(word)
        while index1 + index2 < len(text) + 1:
          string_compare = text[index1 : index1 + index2]
          print(string_compare)
          if string_compare == word:
            res.append([index1, index1 + index2 - 1])
          index1 += 1
      res.sort()
      return res

obj = Solution()
print(obj.indexPairs("ababa", ["aba","ab"]))
