class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def helper(self, root):
        if root == None:
            return 0
        right = self.helper(root.right)
        left = self.helper(root.left)
        if right == -1 or left == -1 or abs(right,left) > 1:
            return -1
        return max(right,left) + 1

    def isBalanced(self, root: TreeNode) -> bool:
        return self.helper(root) != -1