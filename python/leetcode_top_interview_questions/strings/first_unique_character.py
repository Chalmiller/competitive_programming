import typing
from collections import OrderedDict

class Solution:
  def firstUniqChar(self, s: str) -> int:
    """
    Task: Find the first non repeating letter within the string and return its index

    Algorithm:
      1. create an ordered dictionary with the counts of letters
      2. iterate through the dictionary for the first letter with value equal to 1
      3. return the index of that letter
    """
    let_cache = OrderedDict()

    for let in s:
      let_cache[let] = let_cache.get(let, 0) + 1

    for k, v in let_cache.items():
      if v == 1:
        return s.index(k)
    
    return -1
