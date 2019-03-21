# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        path_sum_list = []

        def cal_node_path(root):
            if root == None:
                return 0

            left_path = cal_node_path(root.left)
            right_path = cal_node_path(root.right)

            left_path = left_path if left_path > 0 else 0
            right_path = right_path if right_path > 0 else 0

            path_sum_list.append(left_path + root.val + right_path)

            return root.val + (left_path if left_path > right_path else right_path)

        cal_node_path(root)
        return max(path_sum_list)