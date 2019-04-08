# Definition for a binary tree node.
from typing import List


class TreeNode:
    # Definition for a binary tree node.
    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:

        self.max_deep = -1

        def dfs(root: TreeNode, deep: int, tmp_list: List[int]):

            if not root:
                return

            if deep <= self.max_deep:
                deep += 1
                dfs(root.right, deep, tmp_list)
                dfs(root.left, deep, tmp_list)
                deep -= 1
            else:
                tmp_list.append(root.val)
                self.max_deep = deep
                deep += 1
                dfs(root.right, deep, tmp_list)
                dfs(root.left, deep, tmp_list)
                deep -= 1

        res_list = []
        deep = 0
        dfs(root, deep, res_list)

        return res_list