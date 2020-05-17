from typing import *

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.reverse_stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while self.stack:
          # move items over to the reverse_stack
          curr_el = self.stack.pop()
          self.reverse_stack.append(curr_el)
        
        top_el = self.reverse_stack.pop()

        while self.reverse_stack:
          # move the stack back into its queue orientation
          curr_el = self.reverse_stack.pop()
          self.stack.append(curr_el)

        return top_el

    def peek(self) -> int:
        """
        Get the front element.
        """
        while self.stack:
          # move items over to the reverse_stack
          curr_el = self.stack.pop()
          self.reverse_stack.append(curr_el)
        
        top_el = self.reverse_stack[-1]

        while self.reverse_stack:
          # move the stack back into its queue orientation
          curr_el = self.reverse_stack.pop()
          self.stack.append(curr_el)
          
        return top_el

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
