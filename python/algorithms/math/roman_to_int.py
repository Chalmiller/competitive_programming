from typing import *

class Solution:
    def romanToInt(self, s: str) -> int:
        _sum = 0
        index = 0
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L':50, 'C':100, 'D':500, 'M':1000}
        while index < len(s) - 1:
          if s[index] == 'I' and s[index + 1] == 'V':
            _sum += 4
            index += 2
          elif s[index] == 'I' and s[index + 1] == 'X':
            _sum += 9
            index += 2
          elif s[index] == 'X' and s[index + 1] == 'L':
            _sum += 40
            index += 2
          elif s[index] == 'X' and s[index + 1] == 'C':
            _sum += 90
            index += 2
          elif s[index] == 'C' and s[index + 1] == 'D':
            _sum += 400
            index += 2
          elif s[index] == 'C' and s[index + 1] == 'M':
            _sum += 900
            index += 2 
          else:
            _sum += roman_map[s[index]]
            index += 1
        return _sum 