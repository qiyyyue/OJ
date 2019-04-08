# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:

        self.min_depth = 0

        def dsf(root, tmp_depth):
            if not root:
                return
            if not root.left and not root.right:
                if self.min_depth == 0:
                    self.min_depth = tmp_depth
                elif self.min_depth > tmp_depth:
                    self.min_depth = tmp_depth
                return
            tmp_depth += 1
            dsf(root.left, tmp_depth)
            dsf(root.right, tmp_depth)
            tmp_depth -= 1

        tmp_depth = 1
        dsf(root, tmp_depth)
        return self.min_depth