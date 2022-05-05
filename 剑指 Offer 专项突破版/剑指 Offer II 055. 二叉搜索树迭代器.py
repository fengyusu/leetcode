
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.pointer = root
        self.stack = []
        while self.pointer.left:
            self.stack.append(self.pointer)
            self.pointer = self.pointer.left


    def next(self) -> int:
        res = self.pointer.val
        if self.pointer.right:
            self.pointer = self.pointer.right
            while self.pointer.left:
                self.stack.append(self.pointer)
                self.pointer = self.pointer.left
        elif self.stack:
            self.pointer = self.stack.pop()
        else:
            self.pointer = None
        return res


    def hasNext(self) -> bool:
        return True if self.pointer else False



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()