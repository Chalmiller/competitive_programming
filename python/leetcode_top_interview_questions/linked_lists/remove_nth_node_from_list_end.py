# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # two pointer solution
        ptr1, ptr2 = 0, 0
        slow, fast = head, head

        while fast.next and fast.next.next:
          slow = slow.next
          fast = fast.next.next
          ptr1 += 1
          ptr2 += 2
        
        # the length of the list will be equal to fast
        while ptr1 < (ptr2 + 1 - n):
          slow = slow.next
          ptr1 += 1

        slow.next = slow.next.next
        return head
        

        