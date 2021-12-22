from typing import List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        res = []
        q = deque([root])
        direction = True
        while len(q):
            n = len(q)
            cur_level = []
            while n:
                n -= 1
                if direction:
                    cur_node = q.popleft()
                    cur_level.append(cur_node.val)
                    if cur_node.left:
                        q.append(cur_node.left)
                    if cur_node.right:
                        q.append(cur_node.right)
                else:
                    cur_node = q.pop()
                    cur_level.append(cur_node.val)
                    if cur_node.right:
                        q.appendleft(cur_node.right)
                    if cur_node.left:
                        q.appendleft(cur_node.left)
            res.append(cur_level)
            direction = bool(1 - direction)
        return res



