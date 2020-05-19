from typing import *

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        _min_el = min(letters)
        index = 0
        while index < len(letters):
          if letters[index] <= target:
            index += 1
          else:
            return letters[index]
        return _min_el