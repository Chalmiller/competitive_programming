from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        link_list = []
        
        while head:
            link_list.append(head.val)
            head = head.next
            
        r_link_list = reversed(link_list)
        
        return link_list == r_link_list