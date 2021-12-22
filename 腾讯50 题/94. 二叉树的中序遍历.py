
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        p = root
        stack = []
        while len(stack) or p:
            while p:
                stack.append(p)
                p = p.left
            p = stack.pop()
            res.append(p.val)
            if p.right:
                p = p.right
            else:
                p = None
        return res
