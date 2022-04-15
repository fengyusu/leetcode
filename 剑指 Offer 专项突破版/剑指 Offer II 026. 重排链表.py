
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:


    def reorderList(self, head: ListNode) -> None:

        node_vec = []
        p = head
        while p:
            node_vec.append(p)
            p = p.next
        n = len(node_vec)
        for i in range(n//2):
            j = n-i-1
            tmp = node_vec[i].next
            node_vec[i].next = node_vec[j]
            node_vec[j].next = tmp
        node_vec[n//2].next = None




