
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def helper(self, root: TreeNode, targetSum: int):
        if root is None:
            return 0
        count = 0
        if root.val == targetSum:
            count = 1
        return count + self.helper(root.left, targetSum - root.val) + self.helper(root.right, targetSum - root.val)


    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if root is None:
            return 0
        return self.helper(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
