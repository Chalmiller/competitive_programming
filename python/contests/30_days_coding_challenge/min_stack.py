# Min Stack
from typing import *

class MinStack:

  def __init__(self):
      self.q = []

  # @param x, an integer
  # @return an integer
  def push(self, x):
      curMin = self.getMin()
      if curMin == None or x < curMin:
          curMin = x
      self.q.append((x, curMin));

  # @return nothing
  def pop(self):
      self.q.pop()


  # @return an integer
  def top(self):
      if len(self.q) == 0:
          return None
      else:
          return self.q[len(self.q) - 1][0]


  # @return an integer
  def getMin(self):
      if len(self.q) == 0:
          return None
      else:
          return self.q[len(self.q) - 1][1]
        

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
obj.pop()
print(obj.top())
print(obj.getMin())