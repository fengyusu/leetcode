

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        n = len(postorder)
        if n == 0:
            return None
        cur_val = postorder[-1]
        node = TreeNode(cur_val)
        if n == 1:
            return node
        mid_idx = inorder.index(cur_val)
        node.left = self.buildTree(inorder[0:mid_idx], postorder[0:mid_idx])
        node.right = self.buildTree(inorder[mid_idx+1:], postorder[mid_idx:-1])
        return node
