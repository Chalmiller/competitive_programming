from typing import *

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self._array_queue = []
        self._window = size
        self._size = 0
        

    def next(self, val: int) -> float:
        if self._size < self._window:
            self._array_queue.append(val)
            self._size += 1
            return sum(self._array_queue)/self._size
        else:
            self._array_queue.pop(0)
            self._array_queue.append(val)
            return sum(self._array_queue)/self._window
        
        
# Your MovingAverage object will be instantiated and called as such:
obj = MovingAverage(3)
param_1 = obj.next(1)
param_1 = obj.next(10)
param_1 = obj.next(3)
param_1 = obj.next(5)