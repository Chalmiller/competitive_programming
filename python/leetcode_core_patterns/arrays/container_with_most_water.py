import unittest
from typing import *

class Solution:
    def maxArea(self, height):
      # """
      #   Task: Determine the greatest area of water held within the tank
      #   Intuition: Seems like a good time for a sliding window
        
      #   Algorithm:
      #       - sliding window from each starting point
      #       - take max each time
      #       - return the max
      # """
      _max_area = 0
      
      for i in range(len(height) - 1):
          for j in range(i + 1, len(height)):
              dist = j - i
              _min = min(height[i], height[j])
              curr_area = _min * dist
              _max_area = max(_max_area, curr_area)
      return _max_area

class TestMaxArea(unittest.TestCase):

  def regular_quant(self):
    self.assertEquals(49, Solution().maxArea([1,8,6,2,5,4,8,3,7]))

if __name__ == "__main__":
  unittest.main()
        
