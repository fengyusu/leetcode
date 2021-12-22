from utils import *
class Solution:
    def removeElements0(self, head: ListNode, val: int) -> ListNode:
        new_head = ListNode()
        new_head.next = head
        pre = new_head
        cur = head
        while cur:
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        return new_head.next

    def removeElements(self, head: ListNode, val: int) -> ListNode:
        new_head = ListNode()
        new_head.next = head
        cur = new_head
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return new_head.next

