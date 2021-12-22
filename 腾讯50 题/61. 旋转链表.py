

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None or head.next == None:
            return head
        slow = head
        fast = head
        count = 0
        p = head
        while p:
            p = p.next
            count += 1
        k = k % count
        if k == 0:
            return head
        count  = 0
        while fast.next:
            count += 1
            if count > k:
                slow = slow.next
            fast = fast.next
        res = slow.next
        slow.next = None
        fast.next = head
        return res

print(0b00000011 & 1)