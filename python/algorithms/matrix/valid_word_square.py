from typing import *

class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        ln = len(words)
        for i in range(2*ln-1):
            if i<ln:
                if ln < len(words[i]):
                    return False
                sx = 0
                ex = sy = i
            else:
                sx = i-ln+1
                ex = sy = ln-1
            st = words[sy].ljust(ln)[sx]
            while sx < ex:
                sx += 1
                sy -= 1
                st += words[sy].ljust(ln)[sx]
            if st != st[::-1]:
                return False
        return True