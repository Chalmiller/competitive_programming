from typing import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    """
    Task: Merge two linked lists in non descending order
    Intuition: This is a recursion problem that can be made faster by iteration
    Algorithm:
      - if not l1 return l2 
      - if not l2 return l1
      - if l1.val< l2.val return l1.next = recurse
      - ^ same for l2
    """
    if not l1: return l2
    elif not l2: return l1
    elif l1.val < l2.val:
      l1.next = self.mergeTwoLists(l1.next, l2)
      return l1
    elif l1.val > l2.val:
      l2.next = self.mergeTwoLists(l1, l2.next)
      return l2
    
    