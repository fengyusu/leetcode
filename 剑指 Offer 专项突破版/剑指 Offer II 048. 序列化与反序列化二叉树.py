# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        if root is None:
            return ""

        inorder_list = []
        preorder_list = []
        def inorder(root):
            if root.left:
                inorder(root.left)
            inorder_list.append(str(root.val))
            if root.right:
                inorder(root.right)
        def preorder(root):
            preorder_list.append(str(root.val))
            if root.left:
                preorder(root.left)
            if root.right:
                preorder(root.right)

        inorder(root)
        preorder(root)

        res = "".join(preorder_list+inorder_list)
        print(res)

        return res

    def deserialize(self, data):
        n = len(data) // 2
        if n == 0:
            return None
        preorder_list = list(data[0:n])
        inorder_list = list(data[n:])

        def rebuild(preorder_list, pre_l, pre_r,
                    inorder_list, in_l, in_r):
            if pre_l <= pre_r:
                cur_val = (preorder_list[pre_l])
                new_node = TreeNode(int(cur_val))
                cur_inorder_index = inorder_list.index(cur_val)
                left_len = cur_inorder_index - in_l
                new_node.left = rebuild(preorder_list, pre_l+1, pre_l+left_len,
                                        inorder_list, in_l, cur_inorder_index-1)
                new_node.right = rebuild(preorder_list, pre_l+left_len + 1, pre_r,
                                        inorder_list, cur_inorder_index+1, in_r)
                return new_node

        root = rebuild(preorder_list, 0, n-1, inorder_list, 0, n-1)
        return root


    def serialize(self, root):
        if root is None:
            return ""

        preorder_list = []
        def preorder(root):
            preorder_list.append(str(root.val))

            if root.left:
                preorder(root.left)
            else:
                preorder_list.append("None")

            if root.right:
                preorder(root.right)
            else:
                preorder_list.append("None")

        preorder(root)

        res = " ".join(preorder_list)
        print(res)

        return res

    def deserialize(self, data):
        n = len(data)
        if n == 0:
            return None
        preorder_list = data.split()

        def preorder(preorder_list):
            cur_val = preorder_list.pop(0).strip()
            if cur_val == "None" and not cur_val.isdigit():
                return None

            cur_val = int(cur_val)
            cur_node = TreeNode(cur_val)
            cur_node.left = preorder(preorder_list)
            cur_node.right = preorder(preorder_list)
            return cur_node

        root = preorder(preorder_list)
        return root



# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))