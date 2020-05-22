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
    def findMode(self, root: TreeNode) -> List[int]:
        def dfs(node, res):
          if node:
            res.append(node.val)
            dfs(node.right, res)
            dfs(node.left, res)

        result = []
        dfs(root, result)
        counter = collections.Counter(result)
        highest_occuring = sorted(counter.items(), key=lambda x: x[1])
        response = []

        loop = True
        index = 0
        groups = itertools.groupby(highest_occuring, key=lambda x:x[1])
        print(groups)

        return highest_occuring[0][0]

obj = Solution()
print(obj.findMode())