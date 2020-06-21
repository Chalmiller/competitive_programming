from typing import *
from collections import deque

class Solution:
  def letterCasePermutation(self, S: str) -> List[str]:
    """
    Task: Return a list of all possible strings generated from transforming letters fromlower case to upper
        
    Intuition: I think we can use a breadth first search approach here, but we are trying to practice backtracking,
              so I'll use that instead.

    Algorithm:
      1. for every letter in the string, push the next element to the existing lists
      2. breadth first approach
    """
    result = [[]]

    for let in S:
      n = len(result)
      if let.isalpha():
        for i in range(n):
          result.append(result[i][:])
          result[i].append(let.lower())
          result[i+1].append(let.upper())
      else:
        for i in range(n):
          result[i].append(let)

    return map("".join, result)
