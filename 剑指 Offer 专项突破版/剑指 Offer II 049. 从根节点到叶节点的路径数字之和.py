
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def helper(self,root):
        if root is None:
            return [], []
        if root.left is None and root.right is None:
            return [root.val],[1]
        l_leaf,l_level = self.helper(root.left)
        r_leaf, r_level = self.helper(root.right)

        cur_leaf = []
        cur_level = []
        for i in range(len(l_leaf)):
            cur_leaf.append(l_leaf[i] + root.val * (10 ** l_level[i]))
            cur_level.append(l_level[i]+1)
        for i in range(len(r_leaf)):
            cur_leaf.append(r_leaf[i] + root.val * (10 ** r_level[i]))
            cur_level.append(r_level[i]+1)

        return cur_leaf,cur_level



    def sumNumbers(self, root: TreeNode) -> int:
        res,_ = self.helper(root)
        return sum(res)


    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(root, pre_sum):
            if root is None:
                return 0
            cur_sum = pre_sum * 10 + root.val
            if root.left is None and root.right is None:
                return cur_sum
            else:
                return dfs(root.left, cur_sum) + dfs(root.right, cur_sum)
        return dfs(root, 0)



