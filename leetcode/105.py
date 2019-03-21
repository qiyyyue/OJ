#coding: utf8

'''
根据中序与前序构建树
'''

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 1 and len(inorder) == 1:
            return TreeNode(preorder[0])
        elif len(preorder) == 0:
            return None

        root = TreeNode(preorder[0])

        tmp_index = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:1+tmp_index], inorder[:tmp_index])
        root.right = self.buildTree(preorder[1+tmp_index:], inorder[tmp_index+1:])

        return root