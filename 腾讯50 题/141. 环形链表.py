
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False
        fast = head
        slow = head
        while fast:
            if fast.next is None or fast.next.next is None:
                return False
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break
        return True

