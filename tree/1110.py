
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def helper(self, root:TreeNode, to_delete: list[int]):
        if root == None:
            return
        root.left  = self.helper(root.left, to_delete)
        root.right = self.helper(root.right, to_delete)
        if root.val in to_delete:
            if root.left:
                self.forest.append(root.left)
            if root.right:
                self.forest.append(root.right)
            root = None
        return root


    def delNodes(self, root: TreeNode, to_delete: list[int]) -> list[TreeNode]:
        self.forest = []
        root = self.helper(root,to_delete)
        if root:
            self.forest.append(root)

        return self.forest




