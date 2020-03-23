# 1290: Convert Binary Number in Linked Listto Integer

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        bit_list = []
        while head:
            bit_list.insert(0, head.val)
            head = head.next
        return sum([pow(2, index)*bit_val for index, bit_val in enumerate(bit_list)])

head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
obj = Solution()
obj.getDecimalValue(head)