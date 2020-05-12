from typing import *
import collections
import re

def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        pc = Counter(filter(lambda x : x.isalpha(), licensePlate.lower()))
        return min([w for w in words if Counter(w) & pc == pc], key=len) 

         
              

obj = Solution()
print(obj.shortestCompletingWord("1s3 PSt", ["step", "steps", "stripe", "stepple"]))