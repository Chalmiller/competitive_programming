from typing import *
import unittest

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Task: Modify the linked list in place to alternate between start and end
        Intuition: I can do this the long way, which is to reverse the list and create two separate arrays, then merge

        Algorithm:
            - generate an array of the linked list
            - two pointer technique for the beginning and end
            - modiofy the linked list in place with the two pointers
        
        Tiime: O(n)
        Space: O(n)
        """
        def generate_array(node):
            res = []
            while node:
                res.append(node.val)
                node = node.next
            return res

        clone = head
        inorder_array = generate_array(clone)

        dummy = ListNode(0)
        dummy.next = head

        ptr1, ptr2 = 1, len(inorder_array) - 1
        switch = True
        while ptr1 < ptr2:
            if switch:
                head.next = inorder_array[ptr2]
                ptr2 -= 1
            else:
                head.next = inorder_array[ptr1]
                ptr1 += 1
            switch = not switch
        
        return dummy.next
            


        