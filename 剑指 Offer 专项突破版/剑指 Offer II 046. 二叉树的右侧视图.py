from collections import deque
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        node_queue = deque()
        node_queue.appendleft(root)
        res = []
        while node_queue:
            res.append(node_queue[0].val)
            cur_len = len(node_queue)
            while cur_len:
                cur_len -= 1
                cur_node = node_queue.pop()
                if cur_node.left:
                    node_queue.appendleft(cur_node.left)
                if cur_node.right:
                    node_queue.appendleft(cur_node.right)
        return res
