
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        new_node = Node(val=insertVal)
        if head is None:
            new_node.next = new_node
            return new_node
        if head.next == head:
            head.next = new_node
            new_node.next = head
            return head


        prev = head
        cur = head.next
        max_node = prev
        while not (insertVal >= prev.val and insertVal <= cur.val) and cur != head:
            if cur.val < prev.val:
                max_node = prev
            prev = prev.next
            cur = cur.next
        if cur.val < prev.val:
            max_node = prev

        if (insertVal >= prev.val and insertVal <= cur.val):
            prev.next = new_node
            new_node.next = cur
            return head
        else:
            tmp = max_node.next
            max_node.next = new_node
            new_node.next = tmp
            return head
