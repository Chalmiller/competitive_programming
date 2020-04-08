# 1100 Find K-Length Substrings with no Repeat Characters
from typing import *

class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        num_substrings = 0
        char_freq = {}

        for window_start in range(len(S) - K + 1):
          window = S[window_start : window_start + K]
          unique_window = {s for s in window}
          if len(window) == len(unique_window):
            num_substrings += 1
          
        return num_substrings

obj = Solution()
num = obj.numKLenSubstrNoRepeats("home", 5)
print(num)
