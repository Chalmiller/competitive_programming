import typing

class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
      cache_1 = {}
      cache_2 = {}

      for let in s:
        cache_1[let] = cache_1.get(let, 0) + 1

      for let in t:
        cache_2[let] = cache_2.get(let, 0) + 1

      return cache_1 == cache_2
