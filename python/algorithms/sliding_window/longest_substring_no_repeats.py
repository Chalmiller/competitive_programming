# 3: Longest Substring Without repeating Characters
from typing import *

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        win_start = 0
        char_freq = {}

        for win_end in range(len(s)):
          right_char = s[win_end]
          if right_char not in char_freq:
            char_freq[right_char] = 0
          char_freq[right_char] += 1

          if char_freq[right_char] > 1:
            win_start += 1
            char_freq[right_char] -= 1

          max_length = max(win_end - win_start + 1, max_length)
        return max_length

obj = Solution()
num = obj.lengthOfLongestSubstring("pwwkew")
print(num)