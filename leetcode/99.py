#coding: utf8

'''
恢复二叉搜索树
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    pre = None
    first = None
    second = None

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """

        self.dfs(root)

        self.first.val, self.second.val = self.second.val, self.first.val

    def dfs(self, root):
        if root == None:
            return
        self.dfs(root.left)
        if self.pre and self.pre.val >= root.val:
            if self.first == None:
                self.first = self.pre
                self.second = root
            else:
                self.second = root
        self.pre = root
        self.dfs(root.right)