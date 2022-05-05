
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root: return None
        self.res = None

        def inorder(root):
            if not root: return
            inorder(root.left)
            if not self.res and root.val > p.val:
                self.res = root
                return
            inorder(root.right)

        inorder(root)

        return self.res




