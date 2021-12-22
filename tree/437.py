
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSumWithRoot(self, root:TreeNode, targetSum:int)->int:
        if root == None:
            return 0
        count = 1 if root.val == targetSum else 0
        count += self.pathSumWithRoot(root.left, targetSum-root.val)
        count += self.pathSumWithRoot(root.right,targetSum-root.val)
        return count

    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        return self.pathSum(root.left,targetSum) + self.pathSum(root.right,targetSum) + self.pathSumWithRoot(root, targetSum) if root else 0
