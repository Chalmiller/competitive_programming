# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head

        while slow.next and fast.next.next:
          fast = fast.next.next 
          slow = slow.next 
          if slow.val == fast.val:
            return True
        return False
