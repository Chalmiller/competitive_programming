from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        num_list = []
        while head:
            num_list.append(head.val)
            head = head.next
            
        reversed_num_list = num_list[::-1]
        
        return num_list == reversed_num_list