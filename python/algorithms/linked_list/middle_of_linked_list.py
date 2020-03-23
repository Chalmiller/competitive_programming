# 876: Middle of the Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Brute Force Approach
    # def middleNode(self, head: ListNode) -> ListNode:
    #     array_conversion = []
    #     while head:
    #         array_conversion.append(head)
    #         head = head.next
    #     mid = len(array_conversion)//2
    #     return array_conversion.pop(mid)

    # Two Pointer Approach
    def middleNode(self, head: ListNode) -> ListNode:
        if not head.next:
            return head

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
