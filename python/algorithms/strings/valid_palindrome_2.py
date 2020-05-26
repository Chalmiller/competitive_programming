from typing import *

class Solution(object):
    def validPalindrome(self, s):

        if len(s) < 3:
            return len(s)
        
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                break

        if s[i + 1: j + 1] == s[i + 1: j + 1][::-1]:
            return True
        
        return s[i: j] == s[i: j][::-1]

obj = Solution()
print(obj.validPalindrome("abca"))