
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:

        def helper(root: TreeNode):
            l = r = True
            if root.left:
                l = helper(root.left)
                if l:
                    root.left = None
            if root.right:
                r = helper(root.right)
                if r:
                    root.right = None
            return (l and r and (not root.val))

        res = helper(root)
        if res:
            return None
        else:
            return root

