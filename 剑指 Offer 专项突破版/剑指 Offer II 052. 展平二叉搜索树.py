
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.pre_node = None
        self.res = root
        def in_order(root):
            if not root:
                return

            if root.left:
                in_order(root.left)

            if self.pre_node is None:
                self.pre_node = root
                self.res = root
            else:
                print("pre_node", self.pre_node.val)
                print("root", root.val)
                self.pre_node.left = None
                self.pre_node.right = root
                self.pre_node = root

            if root.right:
                in_order(root.right)

        in_order(root)
        return self.res