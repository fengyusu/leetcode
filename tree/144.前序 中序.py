
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        if root == None:
            return []
        ret = []
        stack = [root]
        while len(stack) != 0:
            cur_node = stack.pop()
            ret.append(cur_node.val)
            if cur_node.right:
                stack.append(cur_node.right)
            if cur_node.left:
                stack.append(cur_node.left)
        return ret





    def inorderTraversal(self, root: TreeNode) -> list[int]:
        if root == None:
            return []
        ret = []
        stack = []
        cur_node = root
        while len(stack) != 0 or cur_node:
            if cur_node:
                stack.append(cur_node)
                cur_node = cur_node.left
            else:
                cur_node = stack.pop()
                ret.append(cur_node.val)
                cur_node = cur_node.right

        return ret



