from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: TreeNode) -> list[float]:
        if root == None:
            return []
        q = deque()
        avg = []
        q.append(root)
        while len(q) != 0:
            count = len(q)
            sum = 0
            for i in range(count):
                cur_node = q.popleft()
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)
                sum += cur_node.val
            avg.append(sum/count)
        return avg

