# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.diameter = 0

    def helper(self, root:TreeNode):
        if root == None:
            return -1,-1
        l_diameter,l_depth = self.helper(root.left)
        r_diameter,r_depth = self.helper(root.right)
        max_depth = max(l_depth, r_depth) + 1
        max_diameter = max(l_diameter, r_diameter)
        max_diameter = max(max_diameter, l_depth+r_depth+2)
        return max_diameter,max_depth

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        diameter,_ = self.helper(root)
        return diameter
