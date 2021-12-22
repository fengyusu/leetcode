
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorder(self, root):
        if root == None:
            return

        if root.left:
            self.inorder(root.left)

        if self.prev and root.val < self.prev.val:
            if self.mistake1 == None:
                self.mistake1 = self.prev
                self.mistake2 = root
            else:
                self.mistake2 = root
        self.prev = root

        if root.right:
            self.inorder(root.right)

    def recoverTree(self, root: TreeNode) -> None:
        self.prev = None
        self.mistake1 = None
        self.mistake2 = None
        self.inorder(root)
        if self.mistake1 and self.mistake2:
            self.mistake1.val,self.mistake2.val = self.mistake2.val,self.mistake1.val
