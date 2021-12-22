

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        p = head
        n = p.next
        while p and n:
            prev.next = n
            p.next = n.next
            n.next = p
            prev = p
            p = prev.next
            if p:
                n = p.next
        return dummy.next
