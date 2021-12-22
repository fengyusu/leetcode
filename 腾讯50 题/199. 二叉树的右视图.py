from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        res = []
        q = deque()
        q.append(root)
        while len(q):
            cur_size = len(q)
            while cur_size:
                cur_size -= 1
                cur_node = q.popleft()
                if cur_size == 0:
                    res.append(cur_node.val)
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)
        return res

