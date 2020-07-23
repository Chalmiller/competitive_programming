from collections import defaultdict
from typing import *

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_collection = defaultdict(list)
        res = []

        for el in strs:
          anagram = sorted(el)
          word_collection[anagram].append(el)

        for els in word_collection.values():
          res.append(els)

        return res
