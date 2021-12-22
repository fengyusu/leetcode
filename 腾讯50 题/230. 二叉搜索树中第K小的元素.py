
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorder(self, root, k):
        if root is None:
            return
        if root.left:
            self.inorder(root.left, k)

        self.count += 1
        if self.count == k:
            self.kthsmall = root.val

        if root.right:
            self.inorder(root.right, k)
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.count = 0
        self. kthsmall = None
        self.inorder(root, k)
        return self.kthsmall