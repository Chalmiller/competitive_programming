# 993: Cousins in Binary Tree
from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool: 
        current = [root]
        while current:
            temp = []
            m = {}
            for node in current:
                for child in [node.left, node.right]:
                    if child:
                        temp.append(child)
                        m[child.val] = node
            if x not in m and y not in m:
                current = temp
            else:
                return not( (x not in m) or (y not in m) or (m[x] == m[y]))

obj = Solution()
num = obj.isCousins([1,2,3,4], 4, 3)
print(num)

        