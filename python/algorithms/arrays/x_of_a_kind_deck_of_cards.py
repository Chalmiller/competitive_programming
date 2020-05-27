from typing import *
import itertools

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        deck.sort()

        if len(deck) < 2:
          return False

        card_groups = itertools.groupby(deck)
        res = []

        for card, group in card_groups:
          res.append(list(group))

        base_count = len(res[0])
        for group in res:
          if len(group) % base_count != 0:
            return False

        return True

obj = Solution()
print(obj.hasGroupsSizeX([1,1,2,2,2,2]))