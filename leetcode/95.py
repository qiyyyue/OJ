# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:

        def gTrees(l: int, r: int) -> List[TreeNode]:
            Trees = []
            if l > r:
                return Trees
            for i in range(l, r + 1):
                lTrees = gTrees(l, i - 1)
                rTrees = gTrees(i + 1, r)
                if len(lTrees) == 0 and len(rTrees) == 0:
                    Trees.append(TreeNode(i))
                elif len(lTrees) == 0:
                    for rTree in rTrees:
                        nTree = TreeNode(i)
                        nTree.right = rTree
                        Trees.append(nTree)
                elif len(rTrees) == 0:
                    for lTree in lTrees:
                        nTree = TreeNode(i)
                        nTree.left = lTree
                        Trees.append(nTree)
                else:
                    for lTree in lTrees:
                        for rTree in rTrees:
                            nTree = TreeNode(i)
                            nTree.left = lTree
                            nTree.right = rTree
                            Trees.append(nTree)
            return Trees

        return gTrees(1, n)