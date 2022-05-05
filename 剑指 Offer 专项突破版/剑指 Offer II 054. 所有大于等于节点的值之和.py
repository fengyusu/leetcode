
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:

        self.pre_sum = 0
        def inorder(root):
            if root is None:
                return
            inorder(root.right)
            self.pre_sum += root.val
            root.val = self.pre_sum
            inorder(root.left)

        inorder(root)
        return root
