from typing import *
import collections

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        seen = set()

        used = [False for i in tiles]
        print(used)
        self.search(tiles, used, '', seen)
        return len(seen)

    def search(self, tiles, used, seq, seen):
      for i in range(len(used)):
        if not used[i]:
          new_seq = seq + tiles[i]
          print(new_seq, used)
          if new_seq not in seen:
            seen.add(new_seq)
            used[i] = True
            self.search(tiles, used, new_seq, seen)
            used[i] = False

obj = Solution()
print(obj.numTilePossibilities("AAB"))
