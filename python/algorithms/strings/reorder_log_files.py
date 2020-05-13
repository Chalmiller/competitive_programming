from typing import *

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
      def f(log):
        id_, rest = log.split(" ", 1)
        return (0, rest, id_) if rest[0].isalpha() else (1, )
      
      return sorted(logs, key = f)


obj = Solution()
print(obj.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))