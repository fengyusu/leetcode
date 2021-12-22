
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, left: TreeNode, right: TreeNode) -> bool:
        if left == None and right == None:
            return True
        if left == None or right == None:
            return False
        if left.val != right.val:
            return False
        return self.isSymmetric(left.left, right.right) and self.isSymmetric(left.right, right.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isSymmetric(root.left, root.right) if root else True