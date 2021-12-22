
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxGain(self, root):
        if not root:
            return 0
        leftgain = max(0, self.maxGain(root.left))
        rightgain = max(0, self.maxGain(root.right))
        cur_pathsum = root.val + (leftgain + rightgain)
        self.max_pathsum = max(self.max_pathsum, cur_pathsum)
        return root.val + max(leftgain, rightgain)


    def maxPathSum(self, root: TreeNode) -> int:
        self.max_pathsum = 0
        self.maxGain(root)
        return self.max_pathsum

