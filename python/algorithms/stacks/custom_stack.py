# 1381: Design a stack with increment operation
from typing import *

class CustomStack:

    def __init__(self, maxSize: int):
        self._data = [None] * maxSize
        self._maxSize = maxSize
        self._front = 0
        self._size = 0

    def push(self, x: int) -> None:
        if (self._size == self._maxSize):
            return
        self._data[self._front] = x
        self._front += 1
        self._size += 1

    def pop(self) -> int:
        if self._data[self._front - 1] == None:
            return -1
        val = self._data[self._front - 1]
        self._data[self._front - 1] = None
        self._size -= 1
        self._front -= 1
        return val
        
    def increment(self, k: int, val: int) -> None:
        if k > len(self._data): k = len(self._data)
        for i in range(k):
            if (self._data[i] == None):
                continue
            self._data[i] += val
        return self._data
        
# Your CustomStack object will be instantiated and called as such:
maxSize = 3
obj = CustomStack(3); # Stack is Empty []
obj.push(1);                          # stack becomes [1]
obj.push(2);                          # stack becomes [1, 2]
obj.pop();                            # return 2 --> Return top of the stack 2, stack becomes [1]
obj.push(2);                          # stack becomes [1, 2]
obj.push(3);                          # stack becomes [1, 2, 3]
obj.push(4);                          # stack still [1, 2, 3], Don't add another elements as size is 4
obj.increment(5, 100);                # stack becomes [101, 102, 103]
obj.increment(2, 100);                # stack becomes [201, 202, 103]
obj.pop();                            # return 103 --> Return top of the stack 103, stack becomes [201, 202]
obj.pop();                            # return 202 --> Return top of the stack 102, stack becomes [201]
obj.pop();                            # return 201 --> Return top of the stack 101, stack becomes []
obj.pop();                            # return -1 --> Stack is empty return -1.