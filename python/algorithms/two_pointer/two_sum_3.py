from typing import *

class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.array = []
        

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.array.append(number)
        self.array.sort()
        

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        if len(self.array) > 2:
          i, j = 0, len(self.array) - 1
          
          while i < j:
            curr_sum = self.array[i] + self.array[j]
            if curr_sum > value:
              j -= 1
            elif curr_sum < value:
              i += 1
            else:
              return True
          return False
        elif len(self.array) == 2:
          return (self.array[0] + self.array[1]) == value
        else:
          return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)