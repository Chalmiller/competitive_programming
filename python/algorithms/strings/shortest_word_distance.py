from typing import *

class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        index_1 = [i for i, e in enumerate(words) if e == word1]
        index_2 = [i for i, e in enumerate(words) if e == word2]
        _min = min([abs(i - j) for i in index_1 for j in index_2])

        return _min

obj = Solution()
print(obj.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "coding", "practice"))