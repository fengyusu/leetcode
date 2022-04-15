from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.node_queue = deque()
        self.node_queue.append(root)
        while self.node_queue:
            cur_len = len(self.node_queue)
            flag = False
            while cur_len:
                cur_len -= 1
                cur_node = self.node_queue[-1]
                if cur_node.left:
                    self.node_queue.appendleft(cur_node.left)
                else:
                    flag = True
                    break
                if cur_node.right:
                    self.node_queue.appendleft(cur_node.right)
                    self.node_queue.pop()
                else:
                    flag = True
                    break
            if flag:
                break


    def insert(self, v: int) -> int:
        cur_node = self.node_queue[-1]
        new_node = TreeNode(val=v)
        self.node_queue.appendleft(new_node)
        if cur_node.left:
            cur_node.right = new_node
            self.node_queue.pop()
        else:
            cur_node.left = new_node
        return cur_node.val


    def get_root(self) -> TreeNode:
        return self.root



# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()
