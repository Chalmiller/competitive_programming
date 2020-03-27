# 104: Max Depth of a Binary Tree
from typing import *

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1