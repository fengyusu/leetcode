
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        l_stack = []
        r_stack = []
        left = root
        right = root
        while left.left:
            l_stack.append(left)
            left = left.left
        while right.right:
            r_stack.append(right)
            right = right.right

        while right and left and right != left:
            sum = left.val + right.val
            if sum == k:
                return True
            elif sum < k:
                if left.right:
                    left = left.right
                    while left.left:
                        l_stack.append(left)
                        left = left.left
                elif l_stack:
                    left = l_stack.pop()
                else:
                    left = None
            else:
                if right.left:
                    right = right.left
                    while right.right:
                        r_stack.append(right)
                        right = right.right
                elif r_stack:
                    right = r_stack.pop()
                else:
                    right = None
        return False
