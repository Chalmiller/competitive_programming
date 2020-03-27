# 590 - N-ary Tree Postorder Traversal
from typing import *

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        if root:
            res = []
            for child in root.children:
                res += self.postorder(child)
            result += res
            result.append(root.val)
        return result
