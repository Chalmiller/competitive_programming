from typing import *

class Solution:
    def toHex(self, num: int) -> str:
        enc = "0123456789abcdef"
        neg1 = 0xffffffff
        v = num
        if v == 0:
            return "0"
        if v < 0:
            v = neg1 - abs(v) + 1
        ans = ""
        while v > 0:
            curt = v % 16
            v //= 16
            ans = enc[curt] + ans
        return ans