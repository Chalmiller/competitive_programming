from typing import *

class Solution:
    def areSentencesSimilar(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2):
          return False
        
        if words1 == words2:
          return True
        
        are_pairs = [False] * len(pairs)

        for i, (word1, word2) in enumerate(pairs):
          if (word1 in words1 and word2 in words2) or (word2 in words1 and word1 in words2):
            are_pairs[i] = True
          else:
            return False

        return all(are_pairs)