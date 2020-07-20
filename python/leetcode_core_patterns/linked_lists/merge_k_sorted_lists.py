from typing import *
import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        Task: Merge k sorted lists into a single list
        Intuition: 
          - There are mutliple ways I could go about this. 
          - One way is to iterate through each linked list and make an array, then sort and relink
          - another way is to link directly by iterating through the array 
        """
        big_list = []
        # just iterating through these for now to figure out how to properly approach this problem
        for link in lists:
          while link:
            big_list.append(link.val)
            link = link.next
        print(big_list)
