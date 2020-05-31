from typing import *
import collections
import itertools

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    curVal, curCount = None, 0
    maxCount = 0
    maxList = set()
    
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        self.inorder(root)
        return list(self.maxList)

    def inorder(self, node: TreeNode):
        if not node:
            return
        self.inorder(node.left)
        self.visitNode(node)
        self.inorder(node.right)
    
    def visitNode(self, node: TreeNode):
        if self.curVal == node.val:
            self.curCount += 1
        else:
            self.curCount = 1
            
        self.curVal = node.val
        
        if self.curCount == self.maxCount:
            self.maxList.add(node.val)
        elif self.curCount > self.maxCount:
            self.maxList = set([node.val])
        
        self.maxCount = max(self.curCount, self.maxCount)

obj = Solution()
print(obj.findMode())