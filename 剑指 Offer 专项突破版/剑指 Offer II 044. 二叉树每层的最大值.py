import sys
from typing import List
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        res = []
        queue = deque()
        queue.appendleft(root)
        while queue:
            cur_len = len(queue)
            cur_max = -sys.maxsize
            for i in range(cur_len):
                cur_node = queue.pop()
                cur_max = max(cur_max, cur_node.val)
                if cur_node.left:
                    queue.appendleft(cur_node.left)
                if cur_node.right:
                    queue.appendleft(cur_node.right)
            res.append(cur_max)
        return res