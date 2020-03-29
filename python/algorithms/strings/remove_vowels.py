# 1119: Remove Vowels from a String
from typing import *

class Solution:
    def removeVowels(self, S: str) -> str:
        vowels = {"a", "e", "i", "o", "u"}
        for let in S:
            if let in vowels:
                S = S.replace(let, '')
        return S

        # regex version
        # return re.sub('a|e|i|o|u', '', S)