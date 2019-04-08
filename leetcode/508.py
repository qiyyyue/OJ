# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        count_dict = {}

        def cal_sub_tree(root: TreeNode, count_dict) -> int:
            if not root:
                return 0
            tmp_val = cal_sub_tree(root.left, count_dict) + root.val + cal_sub_tree(root.right, count_dict)
            if tmp_val in count_dict:
                count_dict[tmp_val] += 1
            else:
                count_dict[tmp_val] = 1
            return tmp_val

        cal_sub_tree(root, count_dict)
        count_dict = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
        max_count = count_dict[0][1]
        res_list = []
        for num in count_dict:
            if num[1] >= max_count:
                res_list.append(num[0])
        return res_list