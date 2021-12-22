
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorder(self, root, p, q):
        if root is None:
            return (False, False)

        contain_p = contain_p_l = contain_p_r = False
        contain_q = contain_q_l = contain_q_r = False
        if root.left:
            (contain_p_l, contain_q_l) = self.postorder(root.left, p, q)

        if root.right:
            (contain_p_r, contain_q_r) = self.postorder(root.right, p, q)

        contain_p = contain_p_l or contain_p_r
        contain_q = contain_q_l or contain_q_r
        if root == p:
            contain_p = True
        if root == q:
            contain_q = True
        if not self.found and contain_p and contain_q:
            self.res_node = root
            self.found = True
        print("root", root.val)
        print("contain",(contain_p, contain_q))

        return (contain_p, contain_q)


    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res_node = None
        self.found = False
        self.postorder(root, p, q)
        return self.res_node