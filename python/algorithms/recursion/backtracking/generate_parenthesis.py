from typing import List
import copy

class Solution:
  def parenthesis_rec(self, left, right, n, output, result):
    if left >= n and right >= n:
      result.append(copy.copy(output))
    
    if left < n:
      output += "("
      self.parenthesis_rec(left + 1, right, n, output, result)
      output.pop()

    if right < left:
      output += ")"
      self.parenthesis_rec(left, right + 1, n, output, result)
      output.pop()


  def generateParenthesis(self, n: int) -> List[str]:
    """
    Task: Generate all combinations of well formed parentheses given a n-length

    Algorithm:
      1. 
    """
    output = ""
    result = []
    self.parenthesis_rec(0, 0, n, output, result)
    return result
    


  