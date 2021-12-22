from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def reversList(self, head: ListNode, k):
        dummy = ListNode()
        p = None
        reversed_tail = head
        while head and k:
            k -= 1
            p = head.next
            head.next = dummy.next
            dummy.next = head
            head = p
        return dummy.next, reversed_tail, p

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k <= 1:
            return head
        lens = 0
        p = head
        while p:
            lens += 1
            p = p.next
        g_lens = lens // k
        dummy = ListNode()
        last_tail = dummy
        next_head = head
        for i in range(g_lens):
            last_tail.next, last_tail, next_head = self.reversList(next_head, k)
        last_tail.next = next_head
        return dummy.next


