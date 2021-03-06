from typing import *
from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cnt = Counter()
        for c1, c2 in zip(secret, guess):
            if c1 == c2:
                bulls += 1
            else:
                cnt[c1] += 1
                cnt[c2] -= 1
        cows = len(secret) - bulls - sum(-i for i in cnt.values() if i < 0)
        return f"{bulls}A{cows}B"