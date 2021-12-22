class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        cur_val = preorder[0]
        root = TreeNode(cur_val)
        index = inorder.index(cur_val)
        root.left = self.buildTree(preorder[1:index+1], inorder[0:index])
        root.right = self.buildTree(preorder[index+1:], inorder[index+1:])
        return root