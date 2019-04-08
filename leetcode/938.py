# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:

        def sumT(root: TreeNode) -> int:
            if not root:
                return 0
            return root.val + sumT(root.left) + sumT(root.right)

        def sumL(root: TreeNode, L: int) -> int:
            if not root:
                return 0
            if root.val < L:
                return sumL(root.right, L)
            elif root.val == L:
                return L + sumT(root.right)
            else:
                return root.val + sumT(root.right) + sumL(root.left, L)

        def sumR(root: TreeNode, R: int) -> int:
            if not root:
                return 0
            if root.val > R:
                return sumR(root.left, R)
            elif root.val == R:
                return R + sumT(root.left)
            else:
                return root.val + sumT(root.left) + sumR(root.right, R)

        def sumLR(root: TreeNode, L: int, R: int) -> int:
            if not root:
                return 0
            if L == root.val:
                return L + sumR(root.right, R)
            elif R == root.val:
                return R + sumL(root.left, L)
            elif L < root.val and R < root.val:
                return sumLR(root.left, L, R)
            elif L > root.val and R > root.val:
                return sumLR(root.right, L, R)
            elif L < root.val and R > root.val:
                return root.val + sumL(root.left, L) + sumR(root.right, R)

        return sumLR(root, L, R)