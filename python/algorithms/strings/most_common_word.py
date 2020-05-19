from typing import *
import re
import collections
import heapq

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
      # munge the paragraph
      for c in "!?',;.":
        paragraph = paragraph.replace(c, " ")
      word_counter = collections.Counter(paragraph.lower().split())
      for ban in banned:
        del word_counter[ban]
      
      sorted_counter = sorted(word_counter.items(), key=lambda x: x[1])
      return sorted_counter[::-1][0][0]

obj = Solution()
print(obj.mostCommonWord("a, a, a, a, b,b,b,c, c",
["a"]))
