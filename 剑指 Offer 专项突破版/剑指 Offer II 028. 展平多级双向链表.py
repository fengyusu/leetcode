
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        next_node_stack = []
        dummy = Node()
        dummy.next = head
        p = dummy
        while p.next or len(next_node_stack):
            while p.next and p.next.child is None:
                p = p.next

            if p.next is None :
                if len(next_node_stack):
                    p_tmp = next_node_stack.pop()
                    p_tmp.prev = p
                    p.next = p_tmp
            else:
                tmp_p = p.next
                if tmp_p.next:
                    next_node_stack.append(tmp_p.next)
                tmp_p.next = tmp_p.child
                tmp_p.child.prev = tmp_p
                tmp_p.child = None
                p = p.next

        return dummy.next


