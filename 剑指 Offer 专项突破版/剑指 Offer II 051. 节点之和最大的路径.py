
# Definition for a binary tree node.
import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def helper(self, root):
        if not root:
            return -sys.maxsize,0
        if not root.left and not root.right:
            return root.val,root.val
        l_max_sum, l_in_max_sum = self.helper(root.left)
        r_max_sum, r_in_max_sum = self.helper(root.right)
        cur_in_max_sum = max([l_in_max_sum, r_in_max_sum, 0]) + root.val
        cur_max_sum = max(l_max_sum, r_max_sum)
        cur_max_sum = max([cur_max_sum, l_in_max_sum + root.val + r_in_max_sum, l_in_max_sum + root.val, root.val + r_in_max_sum, root.val])
        return cur_max_sum, cur_in_max_sum

    def maxPathSum(self, root: TreeNode) -> int:
        return self.helper(root)[0]